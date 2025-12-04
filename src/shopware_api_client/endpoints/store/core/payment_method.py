from shopware_api_client.models.payment_method import PaymentMethodBase


class PaymentMethod(PaymentMethodBase):
    media: "Media | None" = None


from .media import Media  # noqa: E402
