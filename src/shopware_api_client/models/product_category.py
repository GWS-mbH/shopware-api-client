from typing import Annotated

from pydantic import Field

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, PhpAssocArray, RefersTo


class ProductCategoryBase(ApiModelBase):
    _identifier = "product_category"

    id: IdField | None = Field(default=None, exclude=True)
    version_id: IdField | None = Field(default=None, exclude=True)
    translated: PhpAssocArray | None = Field(default=None, exclude=True)

    product_id: Annotated[IdField, RefersTo("product")]
    product_version_id: IdField | None = None
    category_id: Annotated[IdField, RefersTo("category")]
    category_version_id: IdField | None = None
