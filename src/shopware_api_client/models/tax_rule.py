from typing import Annotated

from pydantic import AwareDatetime

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import Data, IdField, RefersTo


class TaxRuleBase(ApiModelBase):
    _identifier: str = "tax_rule"

    tax_rule_type_id: Annotated[IdField, RefersTo("tax_rule_type")]
    country_id: Annotated[IdField, RefersTo("country")]
    tax_rate: float
    data: "Data | None" = None
    tax_id: Annotated[IdField, RefersTo("tax")]
    active_from: AwareDatetime | None = None
