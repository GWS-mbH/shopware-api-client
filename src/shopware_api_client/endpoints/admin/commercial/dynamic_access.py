
from shopware_api_client.endpoints.admin.core.product import Product
from shopware_api_client.endpoints.admin.core.rule import Rule

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class DynamicAccessBase(ApiModelBase[EndpointClass]):
    _identifier: str = "dynamic_access"

    product_id: IdField
    rule_id: IdField

class DynamicAccessRelations:
    product: ForeignRelation["Product"]
    rule: ForeignRelation["Rule"]


class DynamicAccess(DynamicAccessBase["DynamicAccessEndpoint"], DynamicAccessRelations):
    pass


class DynamicAccessEndpoint(EndpointBase[DynamicAccess]):
    name = "swag_dynamic_access_product_rule"
    path = "/swag-dynamic-access-product-rule"
    model_class = DynamicAccess
