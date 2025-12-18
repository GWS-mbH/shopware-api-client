from typing import Any

from pydantic import AliasChoices, Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class DocumentBaseConfigBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "document_base_config"

    document_type_id: IdField
    logo_id: IdField | None = None
    name: str
    filename_prefix: str | None = None
    filename_suffix: str | None = None
    global_: bool = Field(..., serialization_alias="global", validation_alias=AliasChoices("global_", "global"))
    document_number: str | None = None
    config: dict[str, Any] | None = Field(default=None)
