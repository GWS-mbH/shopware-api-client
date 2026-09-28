from typing import Annotated, Any

from pydantic import Field

from shopware_api_client.endpoints.base_fields import IdField, RefersTo
from shopware_api_client.fieldsets import FieldSetBase


class VariantListingConfig(FieldSetBase):
    display_parent: bool | None = None
    main_variant_id: Annotated[IdField | None, RefersTo("product")] = None
    configurator_group_config: list[Any] | dict[str, Any] | None = Field(default=None)
