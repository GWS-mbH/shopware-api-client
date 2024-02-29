from typing import TYPE_CHECKING, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import Currency, ProductStream, SalesChannel, SalesChannelDomain


class ProductExportBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_export"

    product_stream_id: IdField = Field(
        ...,
        serialization_alias="productStreamId",
        validation_alias=AliasChoices("product_stream_id", "productStreamId"),
    )
    storefront_sales_channel_id: IdField = Field(
        ...,
        serialization_alias="storefrontSalesChannelId",
        validation_alias=AliasChoices("storefront_sales_channel_id", "storefrontSalesChannelId"),
    )
    sales_channel_id: IdField = Field(
        ..., serialization_alias="salesChannelId", validation_alias=AliasChoices("sales_channel_id", "salesChannelId")
    )
    sales_channel_domain_id: IdField = Field(
        ...,
        serialization_alias="salesChannelDomainId",
        validation_alias=AliasChoices("sales_channel_domain_id", "salesChannelDomainId"),
    )
    currency_id: IdField = Field(
        ..., serialization_alias="currencyId", validation_alias=AliasChoices("currency_id", "currencyId")
    )
    file_name: str = Field(..., serialization_alias="fileName", validation_alias=AliasChoices("file_name", "fileName"))
    access_key: str = Field(
        ..., serialization_alias="accessKey", validation_alias=AliasChoices("access_key", "accessKey")
    )
    encoding: str
    file_format: str = Field(
        ..., serialization_alias="fileFormat", validation_alias=AliasChoices("file_format", "fileFormat")
    )
    include_variants: bool | None = Field(
        default=None,
        serialization_alias="includeVariants",
        validation_alias=AliasChoices("include_variants", "includeVariants"),
    )
    generate_by_cronjob: bool = Field(
        ...,
        serialization_alias="generateByCronjob",
        validation_alias=AliasChoices("generate_by_cronjob", "generateByCronjob"),
    )
    generated_at: AwareDatetime | None = Field(
        default=None, serialization_alias="generatedAt", validation_alias=AliasChoices("generated_at", "generatedAt")
    )
    interval: int
    header_template: str | None = Field(
        default=None,
        serialization_alias="headerTemplate",
        validation_alias=AliasChoices("header_template", "headerTemplate"),
    )
    body_template: str | None = Field(
        default=None, serialization_alias="bodyTemplate", validation_alias=AliasChoices("body_template", "bodyTemplate")
    )
    footer_template: str | None = Field(
        default=None,
        serialization_alias="footerTemplate",
        validation_alias=AliasChoices("footer_template", "footerTemplate"),
    )
    paused_schedule: bool | None = Field(
        default=None,
        serialization_alias="pausedSchedule",
        validation_alias=AliasChoices("paused_schedule", "pausedSchedule"),
    )
    is_running: bool | None = Field(
        default=None, serialization_alias="isRunning", validation_alias=AliasChoices("is_running", "isRunning")
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


class ProductExportRelations:
    product_stream: ClassVar[ForeignRelation["ProductStream"]] = ForeignRelation("ProductStream", "product_stream_id")
    storefront_sales_channel: ClassVar[ForeignRelation["SalesChannel"]] = ForeignRelation(
        "SalesChannel", "storefrontSalesChannel"
    )
    sales_channel: ClassVar[ForeignRelation["SalesChannel"]] = ForeignRelation("SalesChannel", "sales_channel_id")
    sales_channel_domain: ClassVar[ForeignRelation["SalesChannelDomain"]] = ForeignRelation(
        "SalesChannelDomain", "sales_channel_domain_id"
    )
    currency: ClassVar[ForeignRelation["Currency"]] = ForeignRelation("Currency", "currency_id")


class ProductExport(ProductExportBase["ProductExportEndpoint"], ProductExportRelations):
    pass


class ProductExportEndpoint(EndpointBase[ProductExport]):
    name = "product_export"
    path = "/product-export"
    model_class = ProductExport


registry.register_admin(ProductExportEndpoint)
