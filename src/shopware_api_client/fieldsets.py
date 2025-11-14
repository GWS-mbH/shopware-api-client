from pydantic import BaseModel, ConfigDict, AliasGenerator, AliasChoices
from pydantic.alias_generators import to_camel


class FieldSetBase(BaseModel):
    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=lambda field_name: AliasChoices(field_name, to_camel(field_name)),
            serialization_alias=lambda field_name: to_camel(field_name),
        ),
        validate_assignment=True,
    )
