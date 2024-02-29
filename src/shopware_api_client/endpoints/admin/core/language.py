from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import Customer, Locale, Order, ProductReview, ProductSearchKeyword, SalesChannel, SalesChannelDomain


class LanguageBase(ApiModelBase[EndpointClass]):
    _identifier: str = "language"

    parent_id: IdField | None = Field(
        default=None, serialization_alias="parentId", validation_alias=AliasChoices("parent_id", "parentId")
    )
    locale_id: IdField = Field(
        ..., serialization_alias="localeId", validation_alias=AliasChoices("locale_id", "localeId")
    )
    translation_code_id: IdField | None = Field(
        default=None,
        serialization_alias="translationCodeId",
        validation_alias=AliasChoices("translation_code_id", "translationCodeId"),
    )
    name: str
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


class LanguageRelations:
    parent: ClassVar[ForeignRelation["Language"]] = ForeignRelation("Language", "parent_id")
    locale: ClassVar[ForeignRelation["Locale"]] = ForeignRelation("Locale", "locale_id")
    translation_code: ClassVar[ForeignRelation["Locale"]] = ForeignRelation("Locale", "translation_code_id")
    children: ClassVar[ManyRelation["Language"]] = ManyRelation("Language", "children")
    sales_channels: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation("SalesChannel", "salesChannels")
    sales_channel_default_assignments: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation(
        "SalesChannel", "salesChannelDefaultAssignments"
    )
    sales_channel_domains: ClassVar[ManyRelation["SalesChannelDomain"]] = ManyRelation(
        "SalesChannelDomain", "salesChannelDomains"
    )
    customers: ClassVar[ManyRelation["Customer"]] = ManyRelation("Customer", "customers")
    orders: ClassVar[ManyRelation["Order"]] = ManyRelation("Order", "orders")
    product_search_keywords: ClassVar[ManyRelation["ProductSearchKeyword"]] = ManyRelation(
        "ProductSearchKeyword", "productSearchKeywords"
    )
    product_reviews: ClassVar[ManyRelation["ProductReview"]] = ManyRelation("ProductReview", "productReviews")

    """
    Todo:
    newsletter_recipients[NewsletterRecipient], product_keyword_dictionaries[ProductKeywordDictionary],
    product_search_config[ProductSearchConfig]
    """


class Language(LanguageBase["LanguageEndpoint"], LanguageRelations):
    pass


class LanguageEndpoint(EndpointBase[Language]):
    name = "language"
    path = "/language"
    model_class = Language


registry.register_admin(LanguageEndpoint)
