from shopware_api_client.models.order_customer import OrderCustomer as OrderCustomerBase


class OrderCustomer(OrderCustomerBase):
    salutation: "Salutation | None" = None


from .salutation import Salutation  # noqa: E402
