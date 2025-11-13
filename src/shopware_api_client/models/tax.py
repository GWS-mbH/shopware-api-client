from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class TaxBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "tax"

    tax_rate: float
    name: str
    position: int
