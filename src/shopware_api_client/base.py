import asyncio
import json
from datetime import UTC, datetime, timezone
from email.utils import parsedate_to_datetime
from functools import cached_property
from math import ceil
from time import time
from typing import (
    TYPE_CHECKING,
    Any,
    AsyncGenerator,
    Callable,
    Generic,
    Self,
    Type,
    TypeVar,
    cast,
    get_origin,
    overload,
)

import httpx
from pydantic import (
    AliasChoices,
    AliasGenerator,
    AwareDatetime,
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
    model_serializer,
)
from pydantic.alias_generators import to_camel
from pydantic.main import IncEx

from .cache import DictCache, RedisCache
from .endpoints.base_fields import IdField
from .exceptions import (
    SWAPIDataValidationError,
    SWAPIError,
    SWAPIErrorList,
    SWAPIException,
    SWAPIGatewayTimeout,
    SWAPIInternalServerError,
    SWAPIRetryException,
    SWAPIServiceUnavailable,
    SWFilterException,
    SWNoClientProvided,
)
from .logging import logger

if TYPE_CHECKING:
    from redis.asyncio import Redis

APPLICATION_JSON = "application/json"

EndpointClass = TypeVar("EndpointClass", bound="EndpointBase[Any]")
ModelClass = TypeVar("ModelClass", bound="ApiModelBase[Any]")
RETRY_CACHE_KEY = "shopware-api-client:retry:{url}:{method}"
HEADER_X_RATE_LIMIT_LIMIT = "X-Rate-Limit-Limit"
HEADER_X_RATE_LIMIT_REMAINING = "X-Rate-Limit-Remaining"
HEADER_X_RATE_LIMIT_RESET = "X-Rate-Limit-Reset"


class ConfigBase:
    def __init__(
        self,
        url: str,
        retry_after_threshold: int = 60,
        redis_client: "Redis | None" = None,
        local_cache_cleanup_cycle_seconds: int = 10,
    ) -> None:
        self.url = url.rstrip("/")
        self.retry_after_threshold = retry_after_threshold
        self.cache = (
            RedisCache(redis_client)
            if redis_client
            else DictCache(cleanup_cycle_seconds=local_cache_cleanup_cycle_seconds)
        )


class ClientBase:
    api_url: str
    raw: bool
    language_id: IdField | None = None

    def __init__(self, config: ConfigBase, raw: bool = False) -> None:
        self.api_url = config.url
        self.retry_after_threshold = config.retry_after_threshold
        self.cache = config.cache
        self.raw = raw

    async def __aenter__(self) -> "Self":
        client = self.http_client
        assert isinstance(client, httpx.AsyncClient), "http_client must be an instance of httpx.AsyncClient"
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.http_client.aclose()

    async def log_request(self, request: httpx.Request) -> None:
        if not hasattr(request, "_content"):
            await request.aread()
        logger.debug("Request: %s %s - %r <headers: %s>", request.method, request.url, request.content, request.headers)

    async def log_response(self, response: httpx.Response) -> None:
        await response.aread()
        logger.debug(
            "Response: %s - %s - %r <headers: %s>",
            response.status_code,
            response.reason_phrase,
            response.content,
            response.headers,
        )

    @cached_property
    def http_client(self) -> httpx.AsyncClient:
        return self._get_http_client()

    def _get_http_client(self) -> httpx.AsyncClient:
        raise NotImplementedError()

    def _get_headers(self) -> dict[str, str]:
        headers = {"Content-Type": APPLICATION_JSON, "Accept": APPLICATION_JSON}

        if self.language_id is not None:
            headers["sw-language-id"] = str(self.language_id)

        return headers

    @property
    def timeout(self) -> httpx.Timeout:
        client = self.http_client
        return client.timeout

    @timeout.setter
    def timeout(self, timeout: httpx._types.TimeoutTypes) -> None:
        client = self.http_client
        client.timeout = timeout  # type: ignore

    async def sleep_and_increment(self, retry_wait_base: int, retry_count: int) -> int:
        retry_count += 1
        sleep_and_increment = retry_wait_base**retry_count
        logger.debug(f"Try failed, retrying in {sleep_and_increment} seconds.")
        await asyncio.sleep(sleep_and_increment)
        return retry_count

    def get_header_ts(self, header: str | None, fallback_time: float) -> float:
        if header is None:
            return fallback_time

        server_dt = parsedate_to_datetime(header)
        # ensure timezone-aware UTC
        if server_dt.tzinfo is None:
            server_dt = server_dt.replace(tzinfo=timezone.utc)

        return server_dt.timestamp()

    def parse_reset_time(self, headers: httpx.Headers) -> int:
        """Determine reset wait time based on server time"""
        server_ts = self.get_header_ts(headers.get("Date"), time())
        reset_ts = float(headers.get(HEADER_X_RATE_LIMIT_RESET, "0"))
        adjusted_time = reset_ts - server_ts

        return max(0, ceil(adjusted_time))

    def parse_retry_after(self, headers: httpx.Headers) -> int:
        retry_header: str | None = headers.get("Retry-After")
        if retry_header is None:
            return 1

        if retry_header.isdigit():
            return max(1, int(retry_header))

        current_time = time()
        server_ts = self.get_header_ts(headers.get("Date"), current_time)
        retry_ts = self.get_header_ts(retry_header, current_time)
        adjusted_time = retry_ts - server_ts

        return max(1, ceil(adjusted_time))

    async def _make_request(self, method: str, relative_url: str, **kwargs: Any) -> httpx.Response:
        if relative_url.startswith("http://") or relative_url.startswith("https://"):
            url = relative_url
        else:
            url = f"{self.api_url}{relative_url}"
        client = self.http_client

        headers = self._get_headers()
        headers.update(kwargs.pop("headers", {}))

        retry_after_threshold = int(kwargs.pop("retry_after_threshold", self.retry_after_threshold))
        retry_wait_base = int(kwargs.pop("retry_wait_base", 2))
        retries = int(kwargs.pop("retries", 0))
        retry_errors = tuple(
            kwargs.pop("retry_errors", [SWAPIInternalServerError, SWAPIServiceUnavailable, SWAPIGatewayTimeout])
        )
        no_retry_errors = tuple(kwargs.pop("no_retry_errors", []))

        kwargs.setdefault("follow_redirects", True)

        key_base = RETRY_CACHE_KEY.format(
            url=url.removeprefix("https://").removeprefix("http://"),
            method=method,
        )
        x_retry_limit_cache_key = key_base + ":limit"
        x_retry_remaining_cache_key = key_base + ":remaining"
        x_retry_reset_cache_key = key_base + ":reset"
        x_retry_lock_cache_key = key_base + ":lock"
        got_lock = False

        retry_count = 0
        while True:
            x_retry_remaining = await self.cache.get_and_decrement(x_retry_remaining_cache_key)
            if x_retry_remaining is not None and x_retry_remaining <= 0 and not got_lock:
                current_time = int(time())
                reset_time = cast(int, await self.cache.get(x_retry_reset_cache_key)) or 0
                wait_time = max(1, reset_time - current_time)

                if wait_time > retry_after_threshold:
                    raise SWAPIRetryException(
                        f"Retry threshold exceeded for endpoint {url!r}. Threshold: {retry_after_threshold}s, Retry-After: {wait_time}s"
                    )

                await asyncio.sleep(wait_time)

                got_lock = await self.cache.has_lock(x_retry_lock_cache_key, wait_time)
                continue

            try:
                response = await client.request(method, url, headers=headers, **kwargs)
            except httpx.RequestError as exc:
                if retry_count >= retries:
                    raise SWAPIException(f"HTTP client exception ({exc.__class__.__name__}). Details: {str(exc)}")
                retry_count = await self.sleep_and_increment(retry_wait_base, retry_count)
                continue

            # Set retry-cache if headers are present
            if rl_limit := response.headers.get(HEADER_X_RATE_LIMIT_LIMIT):
                x_retry_limit = int(rl_limit)
                wait_time = self.parse_reset_time(response.headers)
                remaining_requests = int(response.headers.get(HEADER_X_RATE_LIMIT_REMAINING))

                tasks = [
                    self.cache.set(x_retry_remaining_cache_key, remaining_requests),
                    self.cache.set(x_retry_limit_cache_key, x_retry_limit),
                ]

                if wait_time > 0:
                    tasks.append(self.cache.set(x_retry_reset_cache_key, int(time()) + wait_time, wait_time))

                await asyncio.gather(*tasks)

                if got_lock:
                    await self.cache.delete(x_retry_lock_cache_key)
                    got_lock = False

            if response.status_code == 429:
                retry_wait_time = self.parse_retry_after(response.headers)
                if retry_wait_time > retry_after_threshold:
                    error = SWAPIError.from_response(response)
                    raise SWAPIRetryException(
                        f"Retry threshold exceeded for endpoint {url!r}. Threshold: {retry_after_threshold}s, Retry-After: {retry_wait_time}s"
                    ) from error

                # If 429 is thrown, Retry-After == X-Rate-Limit-Reset
                await asyncio.gather(
                    self.cache.set(x_retry_reset_cache_key, int(time()) + retry_wait_time, retry_wait_time),
                    asyncio.sleep(retry_wait_time),
                )

            elif response.status_code >= 400:
                # retry other failure codes
                try:
                    errors: list = response.json().get("errors")
                    # ensure `errors` attribute is a list/tuple, fallback to from_response if not
                    if not isinstance(errors, (list, tuple)):
                        raise ValueError("`errors` attribute in json not a list/tuple!")

                    error: SWAPIError | SWAPIErrorList = SWAPIError.from_errors(errors)  # type: ignore
                except ValueError:
                    error: SWAPIError | SWAPIErrorList = SWAPIError.from_response(response)  # type: ignore

                if isinstance(error, SWAPIErrorList) and len(error.errors) == 1:
                    error = error.errors[0]

                if isinstance(error, SWAPIErrorList):
                    if any([isinstance(err, no_retry_errors) for err in error.errors]):
                        raise error

                    if not any([isinstance(err, retry_errors) for err in error.errors]):
                        raise error

                elif isinstance(error, no_retry_errors) or not isinstance(error, retry_errors):
                    raise error

                if retry_count >= retries:
                    raise error

                retry_count = await self.sleep_and_increment(retry_wait_base, retry_count)
            elif response.status_code == 200 and response.headers.get("Content-Type", "").startswith(APPLICATION_JSON):
                # guard against "200 okay" responses with malformed json
                try:
                    setattr(response, "json_cached", response.json())
                    return response
                except json.JSONDecodeError:
                    # retries exhausted?
                    if retry_count >= retries:
                        response.status_code = 500
                        exception = SWAPIError.from_response(response)
                        # prefix details with x-trace-header to
                        exception.detail = (
                            f"x-trace-id: {str(response.headers.get('x-trace-id', 'not-set'))}" + exception.detail
                        )
                        raise exception

                    retry_count = await self.sleep_and_increment(retry_wait_base, retry_count)
            else:
                return response

    async def get(self, relative_url: str, **kwargs: Any) -> httpx.Response:
        return await self._make_request(method="GET", relative_url=relative_url, **kwargs)

    async def post(self, relative_url: str, **kwargs: Any) -> httpx.Response:
        # we need to set a response type, otherwise we don't get one
        relative_url += "?_response=basic" if "?" not in relative_url else "&_response=basic"
        return await self._make_request(method="POST", relative_url=relative_url, **kwargs)

    async def patch(self, relative_url: str, **kwargs: Any) -> httpx.Response:
        # we need to set a reponse type, otherwise we don't get one
        relative_url += "?_response=basic" if "?" not in relative_url else "&_response=basic"
        return await self._make_request(method="PATCH", relative_url=relative_url, **kwargs)

    async def delete(self, relative_url: str, **kwargs: Any) -> httpx.Response:
        return await self._make_request(method="DELETE", relative_url=relative_url, **kwargs)

    async def upload(self, relative_url: str, **kwargs: Any) -> httpx.Response:
        return await self._make_request(
            method="POST", relative_url=relative_url, headers={"Content-Type": "application/octet-stream"}, **kwargs
        )

    async def close(self) -> None:
        await self.http_client.aclose()

    async def bulk_upsert(
        self,
        name: str,
        objs: list[ModelClass] | list[dict[str, Any]],
        fail_silently: bool = False,
        **request_kwargs: Any,
    ) -> dict[str, Any]:
        raise SWAPIException("bulk_upsert is only supported in the admin API")

    async def bulk_delete(
        self,
        name: str,
        objs: list[ModelClass] | list[dict[str, Any]],
        fail_silently: bool = False,
        **request_kwargs: Any,
    ) -> dict[str, Any]:
        raise SWAPIException("bulk_delete is only supported in the admin API")

    def set_language(self, language_id: IdField | None) -> None:
        self.language_id = language_id


class ApiModelBase(BaseModel, Generic[EndpointClass]):
    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=lambda field_name: AliasChoices(field_name, to_camel(field_name)),
            serialization_alias=lambda field_name: to_camel(field_name),
        ),
        validate_assignment=True,
    )

    id: IdField | None = None
    created_at: AwareDatetime = Field(default_factory=lambda: datetime.now(UTC), exclude=True)
    updated_at: AwareDatetime | None = Field(default=None, exclude=True)

    def __init__(self, client: ClientBase | None = None, **kwargs: dict[str, Any]) -> None:
        super().__init__(**kwargs)
        self._client = client

    def __setattr__(self, name: str, value: Any) -> Any:
        from .endpoints.relations import ForeignRelation, ManyRelation

        fields = super().__getattribute__("model_fields")

        if name in fields and get_origin(fields[name].annotation) in [ForeignRelation, ManyRelation]:
            field = super().__getattribute__(name)
            return field.__set__(self, value)

        return super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        from .endpoints.relations import ForeignRelation, ManyRelation

        if name.startswith("__pydantic"):
            return super().__getattribute__(name)

        fields = super().__getattribute__("model_fields")

        # hack to get the actual ForeignKey-Instance
        if name.endswith("__raw") and name[:-5] in fields:
            return super().__getattribute__(name[:-5])

        if name in fields and get_origin(fields[name].annotation) in [ForeignRelation, ManyRelation]:
            field = super().__getattribute__(name)
            return field.__get__(self, type(self))

        return super().__getattribute__(name)

    @model_serializer(mode="wrap")
    def ser_model(self, serializer: Callable[..., dict[str, Any]]) -> dict[str, Any]:
        from .endpoints.relations import ForeignRelation, ManyRelation

        ser_dict = serializer(self)

        # If we don't ask the api for related fields it returns "null" for this field
        # But the API also doesn't like if we send null back, so we need to remove them here
        for field, info in self.model_fields.items():
            if get_origin(info.annotation) in [ForeignRelation, ManyRelation]:
                raw_obj = getattr(self, f"{field}__raw")
                if raw_obj.data is None and not raw_obj.changed:
                    ser_dict.pop(field, None)

                    if info.serialization_alias is not None:
                        ser_dict.pop(info.serialization_alias, None)

        return ser_dict

    @classmethod
    def using(cls: type[Self], client: ClientBase) -> EndpointClass:
        # we want a fresh endpoint
        endpoint: EndpointClass = getattr(client, cls._identifier.get_default()).__class__(client)  # type: ignore
        return endpoint

    def _get_client(self) -> ClientBase:
        if self._client is None:
            raise SWNoClientProvided("Model has no api client set. Use `using` to set a client.")
        return self._client

    def _get_endpoint(self) -> EndpointClass:
        # we want a fresh endpoint
        client = self._get_client()
        endpoint: EndpointClass = getattr(client, self._identifier).__class__(client)  # type: ignore
        return endpoint

    async def save(self, force_insert: bool = False, update_fields: IncEx | None = None) -> Self | dict | None:
        endpoint = self._get_endpoint()

        if force_insert or self.id is None:
            result = await endpoint.create(obj=self)
        else:
            result = await endpoint.update(pk=self.id, obj=self, update_fields=update_fields)

        return result

    async def delete(self) -> bool:
        endpoint = self._get_endpoint()

        # without id we can't delete
        if self.id is None:
            return False

        return await endpoint.delete(pk=self.id)


class EndpointBase(Generic[ModelClass]):
    name: str
    path: str
    model_class: Type[ModelClass]
    raw: bool

    def __init__(self, client: ClientBase):
        self.client = client
        self.raw = client.raw
        self._filter: list[dict[str, Any]] = []
        self._limit: int | None = None
        self._page: int | None = None
        self._sort: list[dict[str, Any]] = []
        self._associations: dict[str, dict[str, Any]] = {}
        self._includes: dict[str, list[str]] = {}

    def _is_search_query(self) -> bool:
        return any([self._filter, self._sort, self._associations, self._includes])

    def _get_data_dict(self) -> dict[str, Any]:
        data: dict[str, Any] = {}

        if self._filter:
            data["filter"] = self._filter

        if self._sort:
            data["sort"] = self._sort

        if self._limit is not None:
            data["limit"] = self._limit

        if self._page is not None:
            data["page"] = self._page

        if self._associations:
            data["associations"] = self._associations

        if self._includes:
            data["includes"] = self._includes

        return data

    def _reset_endpoint(self) -> None:
        self._filter = []
        self._limit = None
        self._page = None
        self._sort = []
        self._associations = {}
        self._includes = {}

    def _serialize_field_name(self, name: str) -> str:
        from .endpoints.relations import ForeignRelation, ManyRelation

        # if a model contains ForwardRefs it may be not complete and missing some aliases
        if not self.model_class.__pydantic_complete__:
            self.model_class.model_rebuild()

        if name == getattr(self.model_class, "_identifier").get_default():
            return name

        field = self.model_class.model_fields[name]

        if get_origin(field.annotation) in [ForeignRelation, ManyRelation]:
            return cast(str, to_camel(name))
        else:
            return self.model_class.model_fields[name].serialization_alias or name

    @overload
    def _parse_response(self, data: list[dict[str, Any]]) -> list[ModelClass]:
        # typing overload
        ...

    @overload
    def _parse_response(self, data: dict[str, Any]) -> ModelClass:
        # typing overload
        ...

    def _parse_response(self, data: list[dict[str, Any]] | dict[str, Any]) -> list[ModelClass] | ModelClass:
        single = False

        if isinstance(data, dict):
            single = True
            data = [data]

        result_list: list[ModelClass] = []
        errors = []

        for entry in data:
            model_class = self.model_class

            try:
                if "attributes" in entry:
                    obj = model_class(client=self.client, id=entry["id"], **entry["attributes"])
                else:
                    obj = model_class(client=self.client, **entry)
            except ValidationError as exc:
                # catch pydantic validation errors, log faulty result with tracking data and attach to errors
                # (errors will be raised after checking all result objects)
                data = dict(id=entry["id"], **entry["attributes"]) if "attributes" in entry else entry
                logger.error(
                    "Invalid Shopware data",
                    extra={"model": self.model_class, "id": data.get("id"), "data": data, "detail": str(exc)},
                )
                errors.append(exc)
                continue

            result_list.append(obj)

        if errors:
            raise SWAPIDataValidationError(errors=errors)

        if single:
            return result_list[0]

        return result_list

    def _parse_data(self, response_dict: dict[str, Any]) -> list[dict[str, Any]]:
        if "data" in response_dict:
            key = "data"
        elif "elements" in response_dict:
            key = "elements"
        else:
            key = None

        data: list[dict[str, Any]] | dict[str, Any] = response_dict[key] if key else response_dict

        if isinstance(data, dict):
            return [data]

        return data

    def _prase_data_single(self, reponse_dict: dict[str, Any]) -> dict[str, Any]:
        return self._parse_data(reponse_dict)[0]

    async def all(self) -> list[ModelClass] | list[dict[str, Any]]:
        data = self._get_data_dict()

        if self._is_search_query():
            result = await self.client.post(f"/search{self.path}", json=data)
        else:
            result = await self.client.get(f"{self.path}", params=data)

        result_data: list[dict[str, Any]] = self._parse_data(result.json())

        self._reset_endpoint()

        if self.raw:
            return result_data

        return self._parse_response(result_data)

    async def get(self, pk: str) -> ModelClass | dict[str, Any]:
        result = await self.client.get(f"{self.path}/{pk}")
        result_data: dict[str, Any] = self._prase_data_single(result.json())

        if self.raw:
            return result_data

        return self._parse_response(result_data)

    async def update(
        self, pk: str, obj: ModelClass | dict[str, Any], update_fields: IncEx | None = None
    ) -> ModelClass | dict[str, Any] | None:
        if isinstance(obj, ApiModelBase):
            data = obj.model_dump_json(by_alias=True, include=update_fields)
        else:
            data = json.dumps(obj)

        result = await self.client.patch(f"{self.path}/{pk}", data=data)
        # 204 - "no data" handling
        if result.status_code == 204:
            return None

        result_data: dict[str, Any] = self._prase_data_single(result.json())

        if self.raw:
            return result_data

        return self._parse_response(result_data)

    async def first(self) -> ModelClass | dict[str, Any] | None:
        self._limit = 1
        result = await self.all()

        self._reset_endpoint()

        # return None instead of an KeyError, if result is empty
        if len(result) == 0:
            return None

        return result[0]

    async def create(self, obj: ModelClass | dict[str, Any]) -> ModelClass | dict[str, Any] | None:
        if isinstance(obj, ApiModelBase):
            data = obj.model_dump_json(by_alias=True)
        else:
            data = json.dumps(obj)

        result = await self.client.post(f"{self.path}", data=data)
        # 204 - "no data" handling
        if result.status_code == 204:
            return None

        result_data: dict[str, Any] = self._prase_data_single(result.json())

        if self.raw:
            return result_data

        return self._parse_response(result_data)

    async def delete(self, pk: str) -> bool:
        response = await self.client.delete(f"{self.path}/{pk}")

        if response.status_code == 204:
            return True

        return False

    async def get_related(self, parent: ModelClass, relation: str) -> list[ModelClass] | list[dict[str, Any]]:
        parent_endpoint = parent._get_endpoint()
        result = await self.client.get(f"{parent_endpoint.path}/{parent.id}/{relation}")
        result_data: list[dict[str, Any]] = self._parse_data(result.json())

        if self.raw:
            return result_data

        return self._parse_response(result_data)

    def select_related(self, **kwargs: Any) -> Self:
        self._associations.update({self._serialize_field_name(field): data for field, data in kwargs.items()})
        return self

    def only(self, **kwargs: list[str]) -> Self:
        for field, data in kwargs.items():
            self._includes[self._serialize_field_name(field)] = [self._serialize_field_name(d) for d in data]

        return self

    def filter(self, **kwargs: Any) -> Self:
        for key, value in kwargs.items():
            filter_term = ""
            filter_type = "equals"

            field_parts = key.split("__")

            if len(field_parts) > 1:
                filter_term = field_parts[-1]

                match filter_term:
                    case "in":
                        filter_type = "equalsAny"
                    case "contains":
                        filter_type = "contains"
                    case "gt":
                        filter_type = "range"
                    case "gte":
                        filter_type = "range"
                    case "lt":
                        filter_type = "range"
                    case "lte":
                        filter_type = "range"
                    case "range":
                        filter_type = "range"
                    case "startswith":
                        filter_type = "prefix"
                    case "endswith":
                        filter_type = "suffix"
                    case _:
                        filter_term = ""

            if field_parts[0] not in self.model_class.model_fields:
                raise SWFilterException(
                    f"Unknown Field: {field_parts[0]}. Available fields: {self.model_class.model_fields.keys()}"
                )

            if filter_term != "":
                field_parts = field_parts[:-1]

            if len(field_parts) >= 2:
                field = "%s.%s" % (
                    self._serialize_field_name(field_parts[0]),
                    ".".join(field_parts[1:]),
                )
            else:
                field = self._serialize_field_name(field_parts[0])

            parameters = {}

            # range has additional parameters
            if filter_type == "range":
                if filter_term == "range":
                    parameters = {"gte": value[0], "lte": value[1]}
                else:
                    parameters = {filter_term: value}

            self._filter.append({"type": filter_type, "field": field, "value": value, "parameters": parameters})

        return self

    async def bulk_upsert(
        self, objs: list[ModelClass] | list[dict[str, Any]], fail_silently: bool = False, **request_kwargs: Any
    ) -> dict[str, Any]:
        return await self.client.bulk_upsert(name=self.name, objs=objs, fail_silently=fail_silently, **request_kwargs)

    async def bulk_delete(
        self, objs: list[ModelClass] | list[dict[str, Any]], fail_silently: bool = False, **request_kwargs: Any
    ) -> dict[str, Any]:
        return await self.client.bulk_delete(name=self.name, objs=objs, fail_silently=fail_silently, **request_kwargs)

    def limit(self, count: int | None) -> "Self":
        self._limit = count
        return self

    def page(self, num: int | None) -> "Self":
        self._page = num
        return self

    def order_by(self, fields: str | tuple[str]) -> "Self":
        if isinstance(fields, str):
            fields = (fields,)

        for field in fields:
            if field.startswith("-"):
                field = field[1:]
                order = "DESC"
            else:
                order = "ASC"

            if field not in self.model_class.model_fields:
                raise SWFilterException(
                    f"Unknown Field: {field}. Available fields: {self.model_class.model_fields.keys()}"
                )
            else:
                field = self._serialize_field_name(field)

            self._sort.append({"field": field, "order": order})

        return self

    async def iter(self, batch_size: int = 100) -> AsyncGenerator[ModelClass | dict[str, Any], None]:
        self._limit = batch_size
        data = self._get_data_dict()
        page = 1

        if self._is_search_query():
            url = f"/search{self.path}"
        else:
            url = self.path

        while True:
            data["page"] = page
            if self._is_search_query():
                result = await self.client.post(url, json=data)
            else:
                result = await self.client.get(url, params=data)

            result_dict: dict[str, Any] = result.json()
            result_data: list[dict[str, Any]] = self._parse_data(result_dict)

            for entry in result_data:
                if self.raw:
                    yield entry
                else:
                    yield self._parse_response(entry)

            if len(result_data) >= self._limit:
                page += 1
            else:
                break
