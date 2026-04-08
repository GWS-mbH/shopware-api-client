from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.customer import CustomerBase


class Customer(CustomerBase, AdminModel["CustomerEndpoint"]):
    group: ForeignRelation["CustomerGroup"] = Field(default=...)
    default_payment_method: ForeignRelation["PaymentMethod"] = Field(default=...)
    sales_channel: ForeignRelation["SalesChannel"] = Field(default=...)
    language: ForeignRelation["Language"] = Field(default=...)
    last_payment_method: ForeignRelation["PaymentMethod"] = Field(default=...)
    default_billing_address: ForeignRelation["CustomerAddress"] = Field(default=...)
    default_shipping_address: ForeignRelation["CustomerAddress"] = Field(default=...)
    salutation: ForeignRelation["Salutation"] = Field(default=...)
    addresses: ManyRelation["CustomerAddress"] = Field(default=...)
    order_customers: ManyRelation["OrderCustomer"] = Field(default=...)
    tags: ManyRelation["Tag"] = Field(default=...)
    promotions: ManyRelation["Promotion"] = Field(default=...)
    product_reviews: ManyRelation["ProductReview"] = Field(default=...)
    recovery_customer: ManyRelation["CustomerRecovery"] = Field(default=...)
    requested_group: ForeignRelation["CustomerGroup"] = Field(default=...)
    bound_sales_channel: ForeignRelation["SalesChannel"] = Field(default=...)
    wishlists: ManyRelation["CustomerWishlist"] = Field(default=...)
    created_by: ForeignRelation["User"] = Field(default=...)
    updated_by: ForeignRelation["User"] = Field(default=...)


class CustomerEndpoint(AdminEndpoint[Customer]):
    name = "customer"
    path = "/customer"
    model_class = Customer


from .customer_address import CustomerAddress  # noqa: E402
from .customer_group import CustomerGroup  # noqa: E402
from .customer_recovery import CustomerRecovery  # noqa: E402
from .customer_wishlist import CustomerWishlist  # noqa: E402
from .language import Language  # noqa: E402
from .order_customer import OrderCustomer  # noqa: E402
from .payment_method import PaymentMethod  # noqa: E402
from .product_review import ProductReview  # noqa: E402
from .promotion import Promotion  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
from .salutation import Salutation  # noqa: E402
from .tag import Tag  # noqa: E402
from .user import User  # noqa: E402
