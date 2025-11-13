from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.models.custom_entity import CustomEntityBase


class CustomEntity(CustomEntityBase, AdminModel["CustomEntityEndpoint"]):
    pass


class CustomEntityEndpoint(AdminEndpoint[CustomEntity]):
    name = "custom_entity"
    path = "/custom-entity"
    model_class = CustomEntity
