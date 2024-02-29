from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import Currency, Language, ProductExport, SalesChannel


class SalesChannelDomainBase(ApiModelBase[EndpointClass]):
    _identifier: str = "sales_channel_domain"

    url: str
    sales_channel_id: IdField = Field(
        ..., serialization_alias="salesChannelId", validation_alias=AliasChoices("sales_channel_id", "salesChannelId")
    )
    language_id: IdField = Field(
        ..., serialization_alias="languageId", validation_alias=AliasChoices("language_id", "languageId")
    )
    currency_id: IdField = Field(
        ..., serialization_alias="currencyId", validation_alias=AliasChoices("currency_id", "currencyId")
    )
    snippet_set_id: IdField = Field(
        ..., serialization_alias="snippetSetId", validation_alias=AliasChoices("snippet_set_id", "snippetSetId")
    )
    hreflang_use_only_locale: bool | None = Field(
        default=None,
        serialization_alias="hreflangUseOnlyLocale",
        validation_alias=AliasChoices("hreflang_use_only_locale", "hreflangUseOnlyLocale"),
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
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


class SalesChannelDomainRelations:
    sales_channel: ClassVar[ForeignRelation["SalesChannel"]] = ForeignRelation("SalesChannel", "sales_channel_id")
    language: ClassVar[ForeignRelation["Language"]] = ForeignRelation("Language", "language_id")
    currency: ClassVar[ForeignRelation["Currency"]] = ForeignRelation("Currency", "currency_id")
    sales_channel_default_hreflang: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation(
        "SalesChannel", "salesChannelDefaultHreflang"
    )
    product_exports: ClassVar[ManyRelation["ProductExport"]] = ManyRelation("ProductExport", "productExports")

    """
    Not yet implemented Relations:
    snippet_set[SnippetSet]
    """


class SalesChannelDomain(SalesChannelDomainBase["SalesChannelDomainEndpoint"], SalesChannelDomainRelations):
    pass


class SalesChannelDomainEndpoint(EndpointBase[SalesChannelDomain]):
    name = "sales_channel_domain"
    path = "/sales-channel-domain"
    model_class = SalesChannelDomain


registry.register_admin(SalesChannelDomainEndpoint)
