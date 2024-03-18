from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class LanguageBase(ApiModelBase[EndpointClass]):
    _identifier: str = "language"

    parent_id: IdField | None = None
    locale_id: IdField
    translation_code_id: IdField | None = None
    name: str
    custom_fields: dict[str, Any] | None = None


class LanguageRelations:
    parent: ForeignRelation["Language"]
    locale: ForeignRelation["Locale"]
    translation_code: ForeignRelation["Locale"]
    children: ManyRelation["Language"]
    sales_channels: ManyRelation["SalesChannel"]
    sales_channel_default_assignments: ManyRelation["SalesChannel"]
    sales_channel_domains: ManyRelation["SalesChannelDomain"]
    customers: ManyRelation["Customer"]
    orders: ManyRelation["Order"]
    product_search_keywords: ManyRelation["ProductSearchKeyword"]
    product_reviews: ManyRelation["ProductReview"]

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


from .customer import Customer  # noqa: E402
from .locale import Locale  # noqa: E402
from .order import Order  # noqa: E402
from .product_review import ProductReview  # noqa: E402
from .product_search_keyword import ProductSearchKeyword  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
from .sales_channel_domain import SalesChannelDomain  # noqa: E402
