from typing import Any

from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class ProductStreamBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "product_stream"

    api_filter: dict[str, Any] | None = Field(default=None, exclude=True)
    invalid: bool | None = Field(default=None, exclude=True)
    name: str
    description: str | None = None
