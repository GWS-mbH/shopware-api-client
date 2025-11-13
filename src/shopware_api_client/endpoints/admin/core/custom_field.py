from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.models.custom_field import CustomFieldBase


class CustomField(CustomFieldBase, AdminModel["CustomFieldEndpoint"]):
    pass


class CustomFieldEndpoint(AdminEndpoint[CustomField]):
    name = "custom_field"
    path = "/custom-field"
    model_class = CustomField
