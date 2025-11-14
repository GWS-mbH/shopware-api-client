from pydantic import Field

from shopware_api_client.base import ApiModelBase


class TaxRuleTypeBase(ApiModelBase):
    _identifier: str = "tax_rule_type"

    technical_name: str = Field(default="", exclude=True)
    position: int
    type_name: str
