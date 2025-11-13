from shopware_api_client.models.shipping_method import ShippingMethodBase


class ShippingMethod(ShippingMethodBase):
    delivery_time: "DeliveryTime | None" = None
    availability_rule: "Rule | None" = None
    prices: list["ShippingMethodPrice"] | None = None
    media: "Media | None" = None
    tags: list["Tag"] | None = None
    tax: "Tax | None" = None


from ..core.delivery_time import DeliveryTime  # noqa: E402
from ..core.media import Media  # noqa: E402
from ..core.rule import Rule  # noqa: E402
from ..core.shipping_method_price import ShippingMethodPrice  # noqa: E402
from ..core.tag import Tag  # noqa: E402
from ..core.tax import Tax  # noqa: E402
