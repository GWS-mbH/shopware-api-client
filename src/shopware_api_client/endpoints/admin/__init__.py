from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...client import AdminClient

from .commercial.b2b_components_role import B2bComponentsRole, B2bComponentsRoleEndpoint
from .commercial.b2b_employee import B2bEmployee, B2bEmployeeEndpoint
from .commercial.dynamic_access import DynamicAccess, DynamicAccessEndpoint
from .core.acl_role import AclRole, AclRoleEndpoint
from .core.api_info import ApiInfo, ApiInfoEndpoint
from .core.app import App, AppEndpoint
from .core.app_script_condition import AppScriptCondition, AppScriptConditionEndpoint
from .core.category import Category, CategoryEndpoint
from .core.cms_block import CmsBlock, CmsBlockEndpoint
from .core.cms_page import CmsPage, CmsPageEndpoint
from .core.cms_section import CmsSection, CmsSectionEndpoint
from .core.cms_slot import CmsSlot, CmsSlotEndpoint
from .core.country import Country, CountryEndpoint
from .core.country_state import CountryState, CountryStateEndpoint
from .core.currency import Currency, CurrencyEndpoint
from .core.currency_country_rounding import CurrencyCountryRounding, CurrencyCountryRoundingEndpoint
from .core.custom_entity import CustomEntity, CustomEntityEndpoint
from .core.custom_field import CustomField, CustomFieldEndpoint
from .core.customer import Customer, CustomerEndpoint
from .core.customer_address import CustomerAddress, CustomerAddressEndpoint
from .core.customer_group import CustomerGroup, CustomerGroupEndpoint
from .core.customer_recovery import CustomerRecovery, CustomerRecoveryEndpoint
from .core.customer_wishlist import CustomerWishlist, CustomerWishlistEndpoint
from .core.customer_wishlist_product import CustomerWishlistProduct, CustomerWishlistProductEndpoint
from .core.delivery_time import DeliveryTime, DeliveryTimeEndpoint
from .core.document import Document, DocumentEndpoint
from .core.document_base_config import DocumentBaseConfig, DocumentBaseConfigEndpoint
from .core.document_base_config_sales_channel import (
    DocumentBaseConfigSalesChannel,
    DocumentBaseConfigSalesChannelEndpoint,
)
from .core.document_type import DocumentType, DocumentTypeEndpoint
from .core.integration import Integration, IntegrationEndpoint
from .core.landing_page import LandingPage, LandingPageEndpoint
from .core.language import Language, LanguageEndpoint
from .core.locale import Locale, LocaleEndpoint
from .core.main_category import MainCategory, MainCategoryEndpoint
from .core.media import Media, MediaEndpoint
from .core.media_default_folder import MediaDefaultFolder, MediaDefaultFolderEndpoint
from .core.media_folder import MediaFolder, MediaFolderEndpoint
from .core.media_folder_configuration import MediaFolderConfiguration, MediaFolderConfigurationEndpoint
from .core.media_thumbnail import MediaThumbnail, MediaThumbnailEndpoint
from .core.media_thumbnail_size import MediaThumbnailSize, MediaThumbnailSizeEndpoint
from .core.order import Order, OrderEndpoint
from .core.order_address import OrderAddress, OrderAddressEndpoint
from .core.order_customer import OrderCustomer, OrderCustomerEndpoint
from .core.order_delivery import OrderDelivery, OrderDeliveryEndpoint
from .core.order_delivery_position import OrderDeliveryPosition, OrderDeliveryPositionEndpoint
from .core.order_line_item import OrderLineItem, OrderLineItemEndpoint
from .core.order_line_item_download import OrderLineItemDownload, OrderLineItemDownloadEndpoint
from .core.order_transaction import OrderTransaction, OrderTransactionEndpoint
from .core.order_transaction_capture import OrderTransactionCapture, OrderTransactionCaptureEndpoint
from .core.order_transaction_capture_refund import OrderTransactionCaptureRefund, OrderTransactionCaptureRefundEndpoint
from .core.order_transaction_capture_refund_position import (
    OrderTransactionCaptureRefundPosition,
    OrderTransactionCaptureRefundPositionEndpoint,
)
from .core.payment_method import PaymentMethod, PaymentMethodEndpoint
from .core.product import Product, ProductEndpoint
from .core.product_configurator_setting import ProductConfiguratorSetting, ProductConfiguratorSettingEndpoint
from .core.product_cross_selling import ProductCrossSelling, ProductCrossSellingEndpoint
from .core.product_cross_selling_assigned_products import (
    ProductCrossSellingAssignedProducts,
    ProductCrossSellingAssignedProductsEndpoint,
)
from .core.product_download import ProductDownload, ProductDownloadEndpoint
from .core.product_export import ProductExport, ProductExportEndpoint
from .core.product_feature_set import ProductFeatureSet, ProductFeatureSetEndpoint
from .core.product_manufacturer import ProductManufacturer, ProductManufacturerEndpoint
from .core.product_media import ProductMedia, ProductMediaEndpoint
from .core.product_price import ProductPrice, ProductPriceEndpoint
from .core.product_review import ProductReview, ProductReviewEndpoint
from .core.product_search_keyword import ProductSearchKeyword, ProductSearchKeywordEndpoint
from .core.product_stream import ProductStream, ProductStreamEndpoint
from .core.product_visibility import ProductVisibility, ProductVisibilityEndpoint
from .core.product_warehouse import ProductWarehouse, ProductWarehouseEndpoint
from .core.promotion import Promotion, PromotionEndpoint
from .core.promotion_discount import PromotionDiscount, PromotionDiscountEndpoint
from .core.promotion_discount_prices import PromotionDiscountPrices, PromotionDiscountPricesEndpoint
from .core.property_group import PropertyGroup, PropertyGroupEndpoint
from .core.property_group_option import PropertyGroupOption, PropertyGroupOptionEndpoint
from .core.rule import Rule, RuleEndpoint
from .core.rule_condition import RuleCondition, RuleConditionEndpoint
from .core.sales_channel import SalesChannel, SalesChannelEndpoint
from .core.sales_channel_domain import SalesChannelDomain, SalesChannelDomainEndpoint
from .core.salutation import Salutation, SalutationEndpoint
from .core.seo_url import SeoUrl, SeoUrlEndpoint
from .core.shipping_method import ShippingMethod, ShippingMethodEndpoint
from .core.state_machine import StateMachine, StateMachineEndpoint
from .core.state_machine_history import StateMachineHistory, StateMachineHistoryEndpoint
from .core.state_machine_state import StateMachineState, StateMachineStateEndpoint
from .core.state_machine_transition import StateMachineTransition, StateMachineTransitionEndpoint
from .core.system_config import SystemConfig, SystemConfigEndpoint
from .core.tag import Tag, TagEndpoint
from .core.tax import Tax, TaxEndpoint
from .core.tax_rule import TaxRule, TaxRuleEndpoint
from .core.tax_rule_type import TaxRuleType, TaxRuleTypeEndpoint
from .core.unit import Unit, UnitEndpoint
from .core.user import User, UserEndpoint
from .core.warehouse import Warehouse, WarehouseEndpoint
from .core.warehouse_group import WarehouseGroup, WarehouseGroupEndpoint
from .core.warehouse_group_warehouse import WarehouseGroupWarehouse, WarehouseGroupWarehouseEndpoint

__all__ = [
    "AclRole",
    "AdminEndpoints",
    "B2bComponentsRole",
    "B2bEmployee",
    "ApiInfo",
    "App",
    "AppScriptCondition",
    "Category",
    "CmsBlock",
    "CmsPage",
    "CmsSection",
    "CmsSlot",
    "Country",
    "CountryState",
    "Currency",
    "CurrencyCountryRounding",
    "CustomEntity",
    "CustomField",
    "Customer",
    "CustomerAddress",
    "CustomerGroup",
    "CustomerRecovery",
    "CustomerWishlist",
    "CustomerWishlistProduct",
    "DeliveryTime",
    "Document",
    "DocumentBaseConfig",
    "DocumentBaseConfigSalesChannel",
    "DocumentType",
    "DynamicAccess",
    "Integration",
    "LandingPage",
    "Language",
    "Locale",
    "MainCategory",
    "Media",
    "MediaDefaultFolder",
    "MediaFolder",
    "MediaFolderConfiguration",
    "MediaThumbnail",
    "MediaThumbnailSize",
    "Order",
    "OrderAddress",
    "OrderCustomer",
    "OrderDelivery",
    "OrderDeliveryPosition",
    "OrderLineItem",
    "OrderLineItemDownload",
    "OrderTransaction",
    "OrderTransactionCapture",
    "OrderTransactionCaptureRefund",
    "OrderTransactionCaptureRefundPosition",
    "PaymentMethod",
    "Product",
    "ProductConfiguratorSetting",
    "ProductCrossSelling",
    "ProductCrossSellingAssignedProducts",
    "ProductDownload",
    "ProductExport",
    "ProductFeatureSet",
    "ProductManufacturer",
    "ProductMedia",
    "ProductPrice",
    "ProductReview",
    "ProductSearchKeyword",
    "ProductStream",
    "ProductVisibility",
    "ProductWarehouse",
    "Promotion",
    "PromotionDiscount",
    "PromotionDiscountPrices",
    "PropertyGroup",
    "PropertyGroupOption",
    "Rule",
    "RuleCondition",
    "SalesChannel",
    "SalesChannelDomain",
    "Salutation",
    "SeoUrl",
    "ShippingMethod",
    "StateMachine",
    "StateMachineHistory",
    "StateMachineState",
    "StateMachineTransition",
    "SystemConfig",
    "Tag",
    "Tax",
    "TaxRule",
    "TaxRuleType",
    "Unit",
    "User",
    "Warehouse",
    "WarehouseGroup",
    "WarehouseGroupWarehouse",
]


class AdminEndpoints:
    async def load_custom_entities(self, client: "AdminClient") -> None:
        from types import new_class
        from typing import Any

        from pydantic import AwareDatetime, create_model

        from ...base import ApiModelBase, EndpointBase
        from ..base_fields import IdField

        async for custom_entity in self.custom_entity.iter():
            assert(isinstance(custom_entity, CustomEntity))
            fields: dict[str, Any] = {}

            for field in custom_entity.fields:
                field_type: Any = str
                field_appendix = ""

                match field["type"]:
                    case "int":
                        field_type = int
                    case "float":
                        field_type = float
                    case "bool":
                        field_type = bool
                    case "many-to-many":
                        continue
                    case "many-to-one":
                        field_appendix = "_id"
                        field_type = IdField
                    case "one-to-many":
                        continue
                    case "one-to-one":
                        field_appendix = "_id"
                        field_type = IdField
                    case "json":
                        field_type = dict
                    case "price":
                        field_type = float
                    case "date":
                        field_type = AwareDatetime
                    case _:
                        field_type = str

                if field["required"]:
                    fields[field["name"] + field_appendix] = (field_type, ...)
                else:
                    fields[field["name"] + field_appendix] = (field_type | None, None)

            fields["_identifier"] = (str, custom_entity.name)

            ce_model: type[ApiModelBase[Any]] = create_model(custom_entity.name, **fields, __base__=ApiModelBase[EndpointBase])

            ce_endpoint = new_class(f"{custom_entity.name}Endpoint", (EndpointBase[ApiModelBase],))
            ce_endpoint.name = custom_entity.name  # type: ignore
            ce_endpoint.path = f"/{custom_entity.name.replace('_', '-')}"  # type: ignore
            ce_endpoint.model_class = ce_model  # type: ignore

            setattr(client, custom_entity.name, ce_endpoint(client))

    def init_endpoints(self, client: "AdminClient") -> None:
        # Commercial
        self.b2b_employee = B2bEmployeeEndpoint(client)
        self.b2b_components_role = B2bComponentsRoleEndpoint(client)
        self.dynamic_access = DynamicAccessEndpoint(client)

        # Core
        self.acl_role = AclRoleEndpoint(client)
        self.api_info = ApiInfoEndpoint(client)
        self.app = AppEndpoint(client)
        self.app_script_condition = AppScriptConditionEndpoint(client)
        self.category = CategoryEndpoint(client)
        self.cms_block = CmsBlockEndpoint(client)
        self.cms_page = CmsPageEndpoint(client)
        self.cms_section = CmsSectionEndpoint(client)
        self.cms_slot = CmsSlotEndpoint(client)
        self.country = CountryEndpoint(client)
        self.country_state = CountryStateEndpoint(client)
        self.currency = CurrencyEndpoint(client)
        self.currency_country_rounding = CurrencyCountryRoundingEndpoint(client)
        self.custom_entity = CustomEntityEndpoint(client)
        self.custom_field = CustomFieldEndpoint(client)
        self.customer = CustomerEndpoint(client)
        self.customer_address = CustomerAddressEndpoint(client)
        self.customer_group = CustomerGroupEndpoint(client)
        self.customer_recovery = CustomerRecoveryEndpoint(client)
        self.customer_wishlist = CustomerWishlistEndpoint(client)
        self.customer_wishlist_product = CustomerWishlistProductEndpoint(client)
        self.delivery_time = DeliveryTimeEndpoint(client)
        self.document = DocumentEndpoint(client)
        self.document_base_config = DocumentBaseConfigEndpoint(client)
        self.document_base_config_sales_channel = DocumentBaseConfigSalesChannelEndpoint(client)
        self.document_type = DocumentTypeEndpoint(client)
        self.integration = IntegrationEndpoint(client)
        self.landing_page = LandingPageEndpoint(client)
        self.language = LanguageEndpoint(client)
        self.locale = LocaleEndpoint(client)
        self.main_category = MainCategoryEndpoint(client)
        self.media = MediaEndpoint(client)
        self.media_default_folder = MediaDefaultFolderEndpoint(client)
        self.media_folder = MediaFolderEndpoint(client)
        self.media_folder_configuration = MediaFolderConfigurationEndpoint(client)
        self.media_thumbnail = MediaThumbnailEndpoint(client)
        self.media_thumbnail_size = MediaThumbnailSizeEndpoint(client)
        self.order = OrderEndpoint(client)
        self.order_address = OrderAddressEndpoint(client)
        self.order_customer = OrderCustomerEndpoint(client)
        self.order_delivery = OrderDeliveryEndpoint(client)
        self.order_delivery_position = OrderDeliveryPositionEndpoint(client)
        self.order_line_item = OrderLineItemEndpoint(client)
        self.order_line_item_download = OrderLineItemDownloadEndpoint(client)
        self.order_transaction = OrderTransactionEndpoint(client)
        self.order_transaction_capture = OrderTransactionCaptureEndpoint(client)
        self.order_transaction_capture_refund = OrderTransactionCaptureRefundEndpoint(client)
        self.order_transaction_capture_refund_position = OrderTransactionCaptureRefundPositionEndpoint(client)
        self.payment_method = PaymentMethodEndpoint(client)
        self.product = ProductEndpoint(client)
        self.product_configurator_setting = ProductConfiguratorSettingEndpoint(client)
        self.product_cross_selling = ProductCrossSellingEndpoint(client)
        self.product_cross_selling_assigned_products = ProductCrossSellingAssignedProductsEndpoint(client)
        self.product_download = ProductDownloadEndpoint(client)
        self.product_export = ProductExportEndpoint(client)
        self.product_feature_set = ProductFeatureSetEndpoint(client)
        self.product_manufacturer = ProductManufacturerEndpoint(client)
        self.product_media = ProductMediaEndpoint(client)
        self.product_price = ProductPriceEndpoint(client)
        self.product_review = ProductReviewEndpoint(client)
        self.product_search_keyword = ProductSearchKeywordEndpoint(client)
        self.product_stream = ProductStreamEndpoint(client)
        self.product_visibility = ProductVisibilityEndpoint(client)
        self.product_warehouse = ProductWarehouseEndpoint(client)
        self.promotion = PromotionEndpoint(client)
        self.promotion_discount = PromotionDiscountEndpoint(client)
        self.promotion_discount_prices = PromotionDiscountPricesEndpoint(client)
        self.property_group = PropertyGroupEndpoint(client)
        self.property_group_option = PropertyGroupOptionEndpoint(client)
        self.rule = RuleEndpoint(client)
        self.rule_condition = RuleConditionEndpoint(client)
        self.sales_channel = SalesChannelEndpoint(client)
        self.sales_channel_domain = SalesChannelDomainEndpoint(client)
        self.salutation = SalutationEndpoint(client)
        self.seo_url = SeoUrlEndpoint(client)
        self.shipping_method = ShippingMethodEndpoint(client)
        self.state_machine = StateMachineEndpoint(client)
        self.state_machine_history = StateMachineHistoryEndpoint(client)
        self.state_machine_state = StateMachineStateEndpoint(client)
        self.state_machine_transition = StateMachineTransitionEndpoint(client)
        self.system_config = SystemConfigEndpoint(client)
        self.tag = TagEndpoint(client)
        self.tax = TaxEndpoint(client)
        self.tax_rule = TaxRuleEndpoint(client)
        self.tax_rule_type = TaxRuleTypeEndpoint(client)
        self.unit = UnitEndpoint(client)
        self.user = UserEndpoint(client)
        self.warehouse = WarehouseEndpoint(client)
        self.warehouse_group = WarehouseGroupEndpoint(client)
        self.warehouse_group_warehouse = WarehouseGroupWarehouseEndpoint(client)
