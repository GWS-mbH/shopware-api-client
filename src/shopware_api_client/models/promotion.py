from typing import Any

from pydantic import AwareDatetime, Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class PromotionBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "promotion"

    name: str
    active: bool
    valid_from: AwareDatetime | None = None
    valid_until: AwareDatetime | None = None
    max_redemptions_global: int | None = None
    max_redemptions_per_customer: int | None = None
    priority: int
    exclusive: bool
    code: str | None = None
    use_codes: bool
    use_individual_codes: bool
    individual_code_pattern: str | None = None
    use_set_groups: bool
    customer_restriction: bool | None = None
    prevent_combination: bool
    order_count: int | None = Field(default=None, exclude=True)
    orders_per_customer_count: dict[str, Any] | None = Field(default=None, exclude=True)
    exclusion_ids: list[IdField] | None = None
