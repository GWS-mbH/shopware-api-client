from typing import Any, Literal, overload

from pydantic import BaseModel, Field
from pydantic.main import IncEx

from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.exceptions import SWAPIMethodNotAvailable


class Bundle(BaseModel):
    css: list[str]
    js: list[str]
    baseUrl: str | None = None
    type: str


class AppBundle(BaseModel):
    active: bool
    integrationId: str
    type: str
    baseUrl: str
    permissions: dict[str, list[str]]
    version: str
    name: str


class ApiInfo(AdminModel["ApiInfoEndpoint"]):
    _identifier = "api_info"

    version: str
    version_revision: str
    admin_worker: dict[str, Any]
    bundles: dict[str, Bundle | AppBundle]
    settings: dict[str, Any]
    license_toggles: dict[str, bool] | None = Field(default=None)


class ApiInfoEndpoint(AdminEndpoint[ApiInfo]):
    name = "adminWorker"
    path = "/_info/config"
    model_class = ApiInfo

    async def delete(self, pk: str) -> bool:
        raise SWAPIMethodNotAvailable()

    @overload
    async def get(self, pk: str, raw: Literal[False]) -> ApiInfo: ...

    @overload
    async def get(self, pk: str, raw: Literal[True]) -> dict[str, Any]: ...

    @overload
    async def get(self, pk: str) -> ApiInfo: ...

    async def get(self, pk: str, raw: bool = False) -> ApiInfo | dict[str, Any]:
        raise SWAPIMethodNotAvailable()

    @overload
    async def create(self, obj: ApiInfo | dict[str, Any], raw: Literal[False]) -> ApiInfo | None: ...

    @overload
    async def create(self, obj: ApiInfo | dict[str, Any], raw: Literal[True]) -> dict[str, Any] | None: ...

    @overload
    async def create(self, obj: ApiInfo | dict[str, Any], raw: bool) -> ApiInfo | dict[str, Any] | None: ...

    @overload
    async def create(self, obj: ApiInfo | dict[str, Any]) -> ApiInfo | None: ...

    async def create(self, obj: ApiInfo | dict[str, Any], raw: bool = False) -> ApiInfo | dict[str, Any] | None:
        raise SWAPIMethodNotAvailable()

    @overload
    async def update(
        self, pk: str, obj: ApiInfo | dict[str, Any], update_fields: IncEx | None, raw: Literal[False]
    ) -> ApiInfo | None: ...

    @overload
    async def update(
        self, pk: str, obj: ApiInfo | dict[str, Any], update_fields: IncEx | None, raw: Literal[True]
    ) -> dict[str, Any] | None: ...

    @overload
    async def update(
        self, pk: str, obj: ApiInfo | dict[str, Any], update_fields: IncEx | None
    ) -> ApiInfo | None: ...

    @overload
    async def update(
        self, pk: str, obj: ApiInfo | dict[str, Any]
    ) -> ApiInfo | None: ...

    async def update(
        self, pk: str, obj: ApiInfo | dict[str, Any], update_fields: IncEx | None = None, raw: bool = False
    ) -> ApiInfo | dict[str, Any] | None:
        raise SWAPIMethodNotAvailable()

    async def bulk_upsert(
        self, objs: list[ApiInfo] | list[dict[str, Any]], fail_silently: bool = False, **request_kwargs: Any
    ) -> dict[str, Any]:
        raise SWAPIMethodNotAvailable()

    async def bulk_delete(
        self, objs: list[ApiInfo] | list[dict[str, Any]], fail_silently: bool = False, **request_kwargs: Any
    ) -> dict[str, Any]:
        raise SWAPIMethodNotAvailable()
