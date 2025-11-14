from pydantic import AwareDatetime

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import Data, IdField


class TaxRuleBase(ApiModelBase):
    _identifier: str = "tax_rule"

    tax_rule_type_id: IdField
    country_id: IdField
    tax_rate: float
    data: "Data | None" = None
    tax_id: IdField
    active_from: AwareDatetime | None = None
