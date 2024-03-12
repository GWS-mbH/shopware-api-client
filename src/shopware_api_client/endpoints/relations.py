from typing import Any, Coroutine, Generic

from ..base import ApiModelBase, EndpointBase, ModelClass
from ..exceptions import SWNoClientProvided


class ForeignRelation(Generic[ModelClass]):
    def __init__(self, model: str, source: str):
        self.model = model
        self.source = source

    def __get__(
        self, instance: "ApiModelBase[Any]", owner: type[Any]
    ) -> Coroutine[Any, Any, ModelClass | dict[str, Any] | None]:
        from ..client import registry

        if (value := getattr(instance, self.source)) is not None:
            model_class: type[ApiModelBase[EndpointBase]] = registry.get_admin_model(self.model)  # type: ignore
            return model_class.using(instance._get_client()).get(pk=value)

        return self.return_none()

    def __set__(self, instance: "ApiModelBase[Any]", value: ModelClass) -> None:
        setattr(instance, self.source, value.id)

    @staticmethod
    async def return_none() -> None:
        return None


class ManyRelation(Generic[ModelClass]):
    def __init__(self, model: str, api_link: str):
        self.model = model
        self.api_link = api_link

    async def fake_async(self, value: Any) -> Any:
        return value

    def __get__(
        self, instance: Any, owner: type[Any]
    ) -> Coroutine[Any, Any, list[ModelClass] | list[dict[str, Any]] | None]:
        from ..client import registry

        model_class: type[ApiModelBase[EndpointBase]] = registry.get_admin_model(self.model)  # type: ignore
        try:
            return model_class.using(instance._get_client()).get_related(instance, relation=self.api_link)
        except SWNoClientProvided:
            return self.fake_async(None)

    def __set__(self, instance: Any, value: list[ModelClass]) -> None:
        setattr(instance, self.api_link, value)
