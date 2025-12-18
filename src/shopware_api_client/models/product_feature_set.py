from typing import Any

from pydantic import Field

from shopware_api_client.base import ApiModelBase


class ProductFeatureSetBase(ApiModelBase):
    _identifier: str = "product_feature_set"

    name: str
    description: str | None = None
    features: dict[str, Any] | None = Field(default=None)
