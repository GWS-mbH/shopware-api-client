from typing import Any, Coroutine, Generic, get_args

from pydantic import GetCoreSchemaHandler, ValidationInfo
from pydantic.alias_generators import to_camel
from pydantic_core import SchemaValidator, core_schema

from ..base import ApiModelBase, ClientBase, ModelClass


class ForeignRelation(Generic[ModelClass]):
    def __init__(self, field_name: str, data: ModelClass | None = None):
        self.field_name: str = field_name
        self.data: ModelClass | None = data
        self.changed: bool = False

    def _ensure_client(self, client: ClientBase | None) -> None:
        if self.data is not None and self.data._client is None:
            self.data._client = client

    @classmethod
    def __get_pydantic_core_schema__(cls, source: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        assert handler.field_name is not None
        data_tp = get_args(source)[0]
        data_schema = handler.generate_schema(data_tp)

        return core_schema.with_default_schema(
            core_schema.with_info_after_validator_function(
                cls._validate,
                core_schema.nullable_schema(data_schema),
                serialization=core_schema.plain_serializer_function_ser_schema(
                    cls._serialize, info_arg=False, return_schema=core_schema.nullable_schema(data_schema)
                ),
                field_name=handler.field_name,
            ),
            default=ForeignRelation(field_name=handler.field_name, data=None),
        )

    @staticmethod
    def _validate(value: ModelClass | None, info: ValidationInfo) -> "ForeignRelation":
        field_name = info.field_name
        assert field_name is not None
        return ForeignRelation(field_name=field_name, data=value)

    @staticmethod
    def _serialize(value: "ForeignRelation[ModelClass]") -> ModelClass | None:
        assert isinstance(value, ForeignRelation)
        if value.data is None:
            return None
        return value.data

    async def _get(self, instance: "ApiModelBase[Any]") -> ModelClass | None:
        related_id = getattr(instance, f"{self.field_name}_id")
        if self.data is not None or related_id is None:
            self._ensure_client(instance._client)
            return self.data

        model_class: type[ModelClass] = get_args(instance.model_fields[self.field_name].annotation)[0]
        data = await model_class.using(instance._get_client()).get(pk=related_id)
        self.data = data
        return self.data

    def __get__(self, instance: "ApiModelBase[Any]", owner: type[Any]) -> Coroutine[Any, Any, ModelClass | None]:
        return self._get(instance=instance)

    def __set__(self, instance: "ApiModelBase[Any]", value: Any) -> None:
        if value is not None:
            model_class: type[ModelClass] = get_args(instance.model_fields[self.field_name].annotation)[0]
            model_class.model_validate(value)

        # Related models passed to the API win against _id fields, but we can try to
        # keep them somehow in sync
        # it also kinda handels the required check
        setattr(instance, f"{self.field_name}_id", getattr(value, "id", None))
        self.data = value
        self.changed = True


class ManyRelation(Generic[ModelClass]):
    def __init__(self, field_name: str, data: list[ModelClass] | None = None):
        self.field_name: str = field_name
        self.data: list[ModelClass] | None = data
        self.changed: bool = False

    def _ensure_client(self, client: ClientBase | None) -> None:
        if self.data is not None:
            for elem in self.data:
                if elem._client is None:
                    elem._client = client

    @classmethod
    def __get_pydantic_core_schema__(cls, source: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        assert handler.field_name is not None
        data_tp = get_args(source)[0]
        data_schema = handler.generate_schema(data_tp)

        return core_schema.with_default_schema(
            core_schema.with_info_after_validator_function(
                cls._validate,
                core_schema.nullable_schema(core_schema.list_schema(data_schema)),
                serialization=core_schema.plain_serializer_function_ser_schema(
                    cls._serialize,
                    info_arg=False,
                    return_schema=core_schema.nullable_schema(core_schema.list_schema(data_schema)),
                ),
                field_name=handler.field_name,
            ),
            default=ManyRelation(field_name=handler.field_name, data=[]),
        )

    @staticmethod
    def _validate(value: list[ModelClass] | None, info: ValidationInfo) -> "ManyRelation":
        field_name = info.field_name
        assert field_name is not None
        return ManyRelation(field_name=field_name, data=value)

    @staticmethod
    def _serialize(value: "ManyRelation[ModelClass]") -> list[ModelClass] | None:
        assert isinstance(value, ManyRelation)
        if value.data is None:
            return None
        return value.data

    async def _get(self, instance: "ApiModelBase[Any]") -> list[ModelClass] | None:
        api_link = to_camel(self.field_name)
        if self.data is not None:
            self._ensure_client(instance._client)
            return self.data

        model_class: type[ModelClass] = get_args(instance.model_fields[self.field_name].annotation)[0]
        data = await model_class.using(instance._get_client()).get_related(instance, relation=api_link)
        self.data = data
        return self.data

    def __get__(self, instance: "ApiModelBase[Any]", owner: type[Any]) -> Coroutine[Any, Any, list[ModelClass] | None]:
        return self._get(instance=instance)

    def __set__(self, instance: "ApiModelBase[Any]", value: Any) -> None:
        model_class: type[ModelClass] = get_args(instance.model_fields[self.field_name].annotation)[0]
        schema = core_schema.list_schema(
            core_schema.model_schema(cls=model_class, schema=model_class.__pydantic_core_schema__)
        )
        validator = SchemaValidator(schema)
        value = validator.validate_python(value)
        self.data = value
        self.changed = True
