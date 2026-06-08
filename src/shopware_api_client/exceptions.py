import json
from typing import Any, TypedDict, TYPE_CHECKING, Union
from collections.abc import Sequence

from httpx import Response
from pydantic import ValidationError

if TYPE_CHECKING:
    from .base import ApiModelBase


class ErrorPointer(TypedDict):
    idx: int
    entity: str | None
    field: str | None
    detail: str
    orig_obj: Union["ApiModelBase", dict[str, Any], None]


class SWException(Exception):
    pass


class SWAPIException(SWException):
    pass


class SWModelException(SWException):
    pass


class SWFilterException(SWModelException):
    pass


class SWAPIConfigException(SWAPIException):
    pass


class SWAPIRetryException(SWAPIException):
    pass


class SWAPIMethodNotAvailable(SWAPIConfigException):
    def __init__(self, msg: str | None = None, *args: list[Any], **kwargs: dict[Any, Any]) -> None:
        if not msg:
            msg = "Method unsupported by this Endpoint"
        super().__init__(msg, *args, **kwargs)


class SWAPIError(SWAPIException):
    def __init__(self, **kwargs: Any) -> None:
        self.id = kwargs.get("id", "")
        self.links = kwargs.get("links", {})
        self.status = kwargs.get("status", "")
        self.code = kwargs.get("code", "")
        self.title = kwargs.get("title", "")
        self.detail = kwargs.get("detail", "")
        self.description = kwargs.get("description", "")
        self.source = kwargs.get("source", {})
        self.meta = kwargs.get("meta", {})
        self.headers = kwargs.get("headers", {})
        self.request = kwargs.get("request", None)
        self.response = kwargs.get("response", None)
        self.pointer_idx = kwargs.get("pointer_idx", None)
        self.pointer_entity = kwargs.get("pointer_entity", None)
        self.pointer_field = kwargs.get("pointer_field", None)
        self.pointer_orig_obj = kwargs.get("pointer_orig_obj", None)

    def __str__(self) -> str:
        return f"Status: {self.status} {self.title} - {self.detail} - {self.source}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self}>"

    @classmethod
    def get_exception_class(cls, status_code: int) -> type["SWAPIError"]:
        match status_code:
            case 400:
                return SWAPIBadRequest
            case 401:
                return SWAPIUnauthorized
            case 403:
                return SWAPIForbidden
            case 404:
                return SWAPINotFound
            case 405:
                return SWAPIMethodNotAllowed
            case 412:
                return SWAPIPreconditionFailed
            case 429:
                return SWAPITooManyRequests
            case 500:
                return SWAPIInternalServerError
            case 501:
                return SWAPINotImplemented
            case 502:
                return SWAPIBadGateway
            case 503:
                return SWAPIServiceUnavailable
            case 504:
                return SWAPIGatewayTimeout
            case 505:
                return SWAPIHTTPVersionNotSupported
            case _:
                return SWAPIError

    @classmethod
    def from_errors(
        cls,
        errors: list[dict[str, Any]],
        response: Response,
        orig_objs: Sequence["ApiModelBase"] | list[dict[str, Any]],
    ) -> "SWAPIErrorList":
        from .base import AdminModel

        errlist: list["SWAPIError"] = []

        for error in errors:
            error.update({"response": response, "request": response.request})
            exception_class = cls.get_exception_class(int(error["status"]))
            if exception_class == SWAPIInternalServerError:
                exception_class = SWAPIInternalServerError.get_subclass(error)

            idx: int | None = None
            field: str | None = None
            if _pointer := error.get("source", {}).get("pointer"):
                segments: list[str] = [s for s in _pointer.split("/") if s]
                for i, seg in enumerate(segments):
                    if seg.isdigit():
                        idx = int(seg)
                        field = "/".join(segments[i + 1 :]) or None
                        break

            if idx is not None:
                error["pointer_idx"] = idx
                error["pointer_field"] = field

                orig_obj = orig_objs[idx] if idx < len(orig_objs) else None
                error["pointer_orig_obj"] = orig_obj

                if isinstance(orig_obj, AdminModel):
                    error["pointer_entity"] = getattr(orig_obj, "_identifier")
                else:
                    parts = response.url.path.split("/")
                    if parts[1] == "api" and len(parts) > 2:
                        if parts[2] == "_action" and parts[3] == "sync":
                            key_field: str | None = error.get("source", {}).get("pointer")
                            key = key_field and key_field.split("/")[1]
                            error["pointer_entity"] = (
                                json.loads(response.request.content)[key].get("entity") if key else None
                            )
                        else:
                            error["pointer_entity"] = parts[2]
                    else:
                        error["pointer_entity"] = None

            errlist.append(exception_class(**error))

        return SWAPIErrorList(errlist)

    @classmethod
    def from_response(cls, response: Response) -> "SWAPIError":
        exception_class = cls.get_exception_class(response.status_code)

        try:
            response.headers["requested-url"] = str(response.request.url)
        except RuntimeError:
            # If the request URL is not available, we can ignore it.
            pass

        return exception_class(
            status=response.status_code,
            title=response.reason_phrase,
            detail=response.text,
            headers=response.headers,
            request=response._request,
            response=response,
        )

    def get_pointed_error(self) -> ErrorPointer | None:
        return (
            {
                "idx": self.pointer_idx,
                "entity": self.pointer_entity,
                "field": self.pointer_field,
                "detail": self.detail,
                "orig_obj": self.pointer_orig_obj,
            }
            if self.pointer_idx is not None
            else None
        )


class SWAPIErrorList(SWAPIException):
    def __init__(self, errors: list[SWAPIError]) -> None:
        self.errors = errors

    def __str__(self) -> str:
        return f"Errors: {self.errors}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self}>"

    def get_pointed_errors(self) -> list[ErrorPointer]:
        error_pointers: list[ErrorPointer] = []
        for error in self.errors:
            if pointer := error.get_pointed_error():
                error_pointers.append(pointer)

        return error_pointers


class SWAPIDataValidationError(SWAPIException):
    def __init__(self, errors: list[ValidationError] | None = None) -> None:
        self.errors = errors if isinstance(errors, (list, tuple)) else []

    def __str__(self) -> str:
        return f"Invalid Shopware data (pydantic). Errors:\n{'\n'.join([str(e) for e in self.errors])}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self}>"


class SWNoClientProvided(SWModelException):
    pass


class SWNoEndpointClass(SWModelException):
    pass


class SWAPIBadRequest(SWAPIError):
    pass


class SWAPIUnauthorized(SWAPIError):
    pass


class SWAPIForbidden(SWAPIError):
    pass


class SWAPINotFound(SWAPIError):
    pass


class SWAPIMethodNotAllowed(SWAPIError):
    pass


class SWAPIPreconditionFailed(SWAPIError):
    pass


class SWAPITooManyRequests(SWAPIError):
    pass


class SWAPIInternalServerError(SWAPIError):
    @classmethod
    def get_subclass(cls, error_data: dict[str, str]) -> "type[SWAPIInternalServerError]":
        if "SQLSTATE" in error_data["detail"]:
            return SWAPISqlError.get_subclass(error_data)
        else:
            return cls


class SWAPISqlError(SWAPIInternalServerError):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.sql_state, self.rdbm_error_code = self.get_sql_error_codes(kwargs["detail"])

    @classmethod
    def get_subclass(cls, error_data: dict[str, str]) -> "type[SWAPISqlError]":
        _, rdbm_error_code = SWAPISqlError.get_sql_error_codes(detail=error_data["detail"])

        match rdbm_error_code:
            case 1062:
                return SWAPISqlDuplicateEntryError
            case 1452:
                return SWAPISqlForeignKeyError
            case _:
                return SWAPISqlError

    @classmethod
    def get_sql_error_codes(cls, detail: str) -> tuple[str, int]:
        """Shopware's error formatting is 'An exception occurred while executing '{SQL}': SQLSTATE[{CODE}]: {label}: {mysql_code} {message}'"""
        start = detail.find("SQLSTATE[")

        bracket_open = start + 9
        bracket_close = detail.find("]", bracket_open)
        sqlstate = detail[bracket_open:bracket_close]

        rest = detail[bracket_close + 1 :]
        token = rest.split(": ", 2)[2].split(" ", 1)[0]
        return sqlstate, int(token)


class SWAPISqlDuplicateEntryError(SWAPISqlError):
    pass


class SWAPISqlForeignKeyError(SWAPISqlError):
    pass


class SWAPINotImplemented(SWAPIError):
    pass


class SWAPIBadGateway(SWAPIError):
    pass


class SWAPIServiceUnavailable(SWAPIError):
    pass


class SWAPIGatewayTimeout(SWAPIError):
    pass


class SWAPIHTTPVersionNotSupported(SWAPIError):
    pass
