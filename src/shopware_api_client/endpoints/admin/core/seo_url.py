from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import Language, SalesChannel


class SeoUrlBase(ApiModelBase[EndpointClass]):
    _identifier: str = "seo_url"

    sales_channel_id: IdField | None = Field(
        default=None,
        serialization_alias="salesChannelId",
        validation_alias=AliasChoices("sales_channel_id", "salesChannelId"),
    )
    language_id: IdField = Field(
        ..., serialization_alias="languageId", validation_alias=AliasChoices("language_id", "languageId")
    )
    foreign_key: IdField = Field(
        ..., serialization_alias="foreignKey", validation_alias=AliasChoices("foreign_key", "foreignKey")
    )
    route_name: str = Field(
        ..., serialization_alias="routeName", validation_alias=AliasChoices("route_name", "routeName")
    )
    path_info: str = Field(..., serialization_alias="pathInfo", validation_alias=AliasChoices("path_info", "pathInfo"))
    seo_path_info: str = Field(
        ..., serialization_alias="seoPathInfo", validation_alias=AliasChoices("seo_path_info", "seoPathInfo")
    )
    is_canonical: bool | None = Field(
        default=None, serialization_alias="isCanonical", validation_alias=AliasChoices("is_canonical", "isCanonical")
    )
    is_modified: bool | None = Field(
        default=None, serialization_alias="isModified", validation_alias=AliasChoices("is_modified", "isModified")
    )
    is_deleted: bool | None = Field(
        default=None, serialization_alias="isDeleted", validation_alias=AliasChoices("is_deleted", "isDeleted")
    )
    url: str | None = Field(default=None, description="Runtime field, cannot be used as part of the criteria.")
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    is_valid: bool | None = Field(
        None,
        alias="isValid",
        description="Runtime field, cannot be used as part of the criteria.",
    )
    created_at: AwareDatetime = Field(
        ..., serialization_alias="createdAt", validation_alias=AliasChoices("created_at", "createdAt"), exclude=True
    )
    updated_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="updatedAt",
        validation_alias=AliasChoices("updated_at", "updatedAt"),
        exclude=True,
    )


class SeoUrlRelations:
    language: ClassVar[ForeignRelation["Language"]] = ForeignRelation("Language", "language_id")
    sales_channel: ClassVar[ForeignRelation["SalesChannel"]] = ForeignRelation("SalesChannel", "sales_channel_id")


class SeoUrl(SeoUrlBase["SeoUrlEndpoint"], SeoUrlRelations):
    pass


class SeoUrlEndpoint(EndpointBase[SeoUrl]):
    name = "seo_url"
    path = "/seo-url"
    model_class = SeoUrl


registry.register_admin(SeoUrlEndpoint)
