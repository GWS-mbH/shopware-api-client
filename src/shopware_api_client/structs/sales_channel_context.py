from shopware_api_client.fieldsets import FieldSetBase

from shopware_api_client.endpoints.store.core.currency import Currency
from shopware_api_client.endpoints.store.core.customer import Customer
from shopware_api_client.endpoints.store.core.customer_group import CustomerGroup
from shopware_api_client.endpoints.store.core.payment_method import PaymentMethod
from shopware_api_client.endpoints.store.core.sales_channel import SalesChannel
from shopware_api_client.endpoints.store.core.shipping_method import ShippingMethod
from shopware_api_client.endpoints.store.core.tax import Tax

from .cash_rounding_config import CashRoundingConfig
from .context import Context
from .language_info import LanguageInfo
from .measurement_units import MeasurementUnits
from .shipping_location import ShippingLocation


class SalesChannelContext(FieldSetBase):
    token: str | None = None
    current_customer_group: CustomerGroup | None = None
    fallback_customer_group: CustomerGroup | None = None
    currency: Currency | None = None
    sales_channel: SalesChannel
    measurementSystem: MeasurementUnits | None = None
    tax_rules: list[Tax] | None = None
    customer: Customer | None = None
    payment_method: PaymentMethod | None = None
    shipping_location: ShippingLocation | None = None
    shipping_method: ShippingMethod | None = None
    context: Context | None = None
    item_rounding: CashRoundingConfig
    total_rounding: CashRoundingConfig
    language_info: LanguageInfo
