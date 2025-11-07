from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.customer import Customer as CustomerBase


class Customer(CustomerBase, AdminModel["CustomerEndpoint"]):
    group: ForeignRelation["CustomerGroup"]
    default_payment_method: ForeignRelation["PaymentMethod"]
    sales_channel: ForeignRelation["SalesChannel"]
    language: ForeignRelation["Language"]
    last_payment_method: ForeignRelation["PaymentMethod"]
    default_billing_address: ForeignRelation["CustomerAddress"]
    default_shipping_address: ForeignRelation["CustomerAddress"]
    salutation: ForeignRelation["Salutation"]
    addresses: ManyRelation["CustomerAddress"]
    order_customers: ManyRelation["OrderCustomer"]
    tags: ManyRelation["Tag"]
    promotions: ManyRelation["Promotion"]
    product_reviews: ManyRelation["ProductReview"]
    recovery_customer: ManyRelation["CustomerRecovery"]
    requested_group: ForeignRelation["CustomerGroup"]
    bound_sales_channel: ForeignRelation["SalesChannel"]
    wishlists: ManyRelation["CustomerWishlist"]
    created_by: ForeignRelation["User"]
    updated_by: ForeignRelation["User"]


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
