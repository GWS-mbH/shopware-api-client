from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.product_stream import ProductStream as ProductStreamBase


class ProductStream(ProductStreamBase, AdminModel["ProductStreamEndpoint"]):
    product_cross_sellings: ManyRelation["ProductCrossSelling"]
    product_exports: ManyRelation["ProductExport"]
    categories: ManyRelation["Category"]

    """
    Todo:
    filters[ProductStreamFilter]
    """


class ProductStreamEndpoint(AdminEndpoint[ProductStream]):
    name = "product_stream"
    path = "/product-stream"
    model_class = ProductStream


from .category import Category  # noqa: E402
from .product_cross_selling import ProductCrossSelling  # noqa: E402
from .product_export import ProductExport  # noqa: E402
