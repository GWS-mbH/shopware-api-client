from shopware_api_client.models.order_customer import OrderCustomerBase


class OrderCustomer(OrderCustomerBase):
    salutation: "Salutation | None" = None


from .salutation import Salutation  # noqa: E402
