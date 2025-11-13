from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.dynamic_access import DynamicAccessBase


class DynamicAccess(DynamicAccessBase, AdminModel["DynamicAccessEndpoint"]):
    product: ForeignRelation["Product"]
    rule: ForeignRelation["Rule"]


class DynamicAccessEndpoint(AdminEndpoint[DynamicAccess]):
    name = "swag_dynamic_access_product_rule"
    path = "/swag-dynamic-access-product-rule"
    model_class = DynamicAccess


from ..core.product import Product  # noqa: E402
from ..core.rule import Rule  # noqa: E402
