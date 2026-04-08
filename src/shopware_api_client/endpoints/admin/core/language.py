from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.language import LanguageBase


class Language(LanguageBase, AdminModel["LanguageEndpoint"]):
    parent: ForeignRelation["Language"] = Field(default=...)
    locale: ForeignRelation["Locale"] = Field(default=...)
    translation_code: ForeignRelation["Locale"] = Field(default=...)
    children: ManyRelation["Language"] = Field(default=...)
    sales_channels: ManyRelation["SalesChannel"] = Field(default=...)
    sales_channel_default_assignments: ManyRelation["SalesChannel"] = Field(default=...)
    sales_channel_domains: ManyRelation["SalesChannelDomain"] = Field(default=...)
    customers: ManyRelation["Customer"] = Field(default=...)
    orders: ManyRelation["Order"] = Field(default=...)
    product_search_keywords: ManyRelation["ProductSearchKeyword"] = Field(default=...)
    product_reviews: ManyRelation["ProductReview"] = Field(default=...)

    """
    Todo:
    newsletter_recipients[NewsletterRecipient], product_keyword_dictionaries[ProductKeywordDictionary],
    product_search_config[ProductSearchConfig]
    """


class LanguageEndpoint(AdminEndpoint[Language]):
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
