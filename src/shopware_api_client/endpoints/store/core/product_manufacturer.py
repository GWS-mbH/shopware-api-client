from shopware_api_client.models.product_manufacturer import ProductManufacturerBase


class ProductManufacturer(ProductManufacturerBase):
    media: "Media | None" = None


from .media import Media  # noqa: E402
