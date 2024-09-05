from ....base import ApiModelBase, EndpointBase, EndpointClass


class CustomFieldBase(ApiModelBase[EndpointClass]):
    _identifier: str = "custom_field"
    
    name: str
    custom_field_set_id: str | None = None


class CustomFieldRelations:
    pass


class CustomField(CustomFieldBase["CustomFieldEndpoint"], CustomFieldRelations):
    pass


class CustomFieldEndpoint(EndpointBase[CustomField]):
    name = "custom_field"
    path = "/custom-field"
    model_class = CustomField
