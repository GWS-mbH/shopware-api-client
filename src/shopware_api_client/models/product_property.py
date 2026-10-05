from typing import Annotated

from pydantic import Field

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, PhpAssocArray, RefersTo


class ProductPropertyBase(ApiModelBase):
    _identifier = "product_property"

    id: IdField | None = Field(default=None, exclude=True)
    version_id: IdField | None = Field(default=None, exclude=True)
    translated: PhpAssocArray | None = Field(default=None, exclude=True)

    product_id: Annotated[IdField, RefersTo("product")]
    product_version_id: IdField | None = None
    option_id: Annotated[IdField, RefersTo("property_group_option")]
