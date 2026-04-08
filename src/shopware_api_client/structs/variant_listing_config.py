from typing import Any

from pydantic import Field

from shopware_api_client.fieldsets import FieldSetBase


class VariantListingConfig(FieldSetBase):
    display_parent: bool | None = None
    main_variant_id: str | None = None
    configurator_group_config: list[Any] | dict[str, Any] | None = Field(default=None)
