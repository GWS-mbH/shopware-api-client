from shopware_api_client.fieldsets import FieldSetBase


class CashRoundingConfig(FieldSetBase):
    decimals: int
    interval: float
    round_for_net: bool
