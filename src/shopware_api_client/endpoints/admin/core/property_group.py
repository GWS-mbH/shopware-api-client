from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.property_group import PropertyGroupBase


class PropertyGroup(PropertyGroupBase, AdminModel["PropertyGroupEndpoint"]):
    options: ManyRelation["PropertyGroupOption"] = Field(default=...)


class PropertyGroupEndpoint(AdminEndpoint[PropertyGroup]):
    name = "property_group"
    path = "/property-group"
    model_class = PropertyGroup


from .property_group_option import PropertyGroupOption  # noqa: E402
