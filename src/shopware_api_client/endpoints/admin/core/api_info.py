from typing import Any

from pydantic import BaseModel

from shopware_api_client.exceptions import SWAPIMethodNotAvailable

from ....base import ApiModelBase, EndpointBase, EndpointClass


class Bundle(BaseModel):
    css: list[str]
    js: list[str]
    base_url: str | None = None
    type: str

class ApiInfoBase(ApiModelBase[EndpointClass]):
    _identifier = "api_info"

    version: str
    version_revision: str
    admin_worker: dict[str, Any]
    bundles: dict[str, Bundle]
    settings: dict[str, Any]
    license_toggles: dict[str, bool] | None = None


class ApiInfo(ApiInfoBase["ApiInfoEndpoint"]):
    pass


class ApiInfoEndpoint(EndpointBase[ApiInfo]):
    name = "adminWorker"
    path = "/_info/config"
    model_class = ApiInfo

    async def delete(self, pk: str) -> bool:
        raise SWAPIMethodNotAvailable("Method unsupported by this Endpoint")
    
    async def get(self, pk: str) -> ApiInfo | dict[str, Any]:
        raise SWAPIMethodNotAvailable("Method unsupported by this Endpoint")

    async def create(self, obj: ApiInfo | dict[str, Any]) -> ApiInfo | dict[str, Any] | None:
        raise SWAPIMethodNotAvailable("Method unsupported by this Endpoint")

    async def update(self, pk: str, obj: ApiInfo | dict[str, Any]) -> ApiInfo | dict[str, Any] | None:
        raise SWAPIMethodNotAvailable("Method unsupported by this Endpoint")

    async def bulk_upsert(
        self, objs: list[ApiInfo] | list[dict[str, Any]], **request_kwargs: Any
    ) -> dict[str, Any] | None:
        raise SWAPIMethodNotAvailable("Method unsupported by this Endpoint")

    async def bulk_delete(self, objs: list[ApiInfo] | list[dict[str, Any]], **request_kwargs: Any) -> dict[str, Any]:
        raise SWAPIMethodNotAvailable("Method unsupported by this Endpoint")