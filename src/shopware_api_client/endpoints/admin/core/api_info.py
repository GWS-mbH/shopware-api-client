from typing import Any

from pydantic import BaseModel
from pydantic.main import IncEx

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
        raise SWAPIMethodNotAvailable()
    
    async def get(self, pk: str) -> ApiInfo | dict[str, Any]:
        raise SWAPIMethodNotAvailable()

    async def create(self, obj: ApiInfo | dict[str, Any]) -> ApiInfo | dict[str, Any] | None:
        raise SWAPIMethodNotAvailable()

    async def update(self, pk: str, obj: ApiInfo | dict[str, Any], update_fields: IncEx = None) -> ApiInfo | dict[str, Any] | None:
        raise SWAPIMethodNotAvailable()

    async def bulk_upsert(
        self, objs: list[ApiInfo] | list[dict[str, Any]], fail_silently: bool = False, **request_kwargs: Any
    ) -> dict[str, Any]:
        raise SWAPIMethodNotAvailable()

    async def bulk_delete(self, objs: list[ApiInfo] | list[dict[str, Any]], fail_silently: bool = False, **request_kwargs: Any) -> dict[str, Any]:
        raise SWAPIMethodNotAvailable()