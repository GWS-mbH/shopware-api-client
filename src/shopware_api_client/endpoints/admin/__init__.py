from typing import Any, TYPE_CHECKING

from ...base import AdminModel

if TYPE_CHECKING:
    from ...client import AdminClient

from .commercial.b2b_components_role import B2bComponentsRole, B2bComponentsRoleEndpoint
from .commercial.b2b_components_shopping_list import B2bComponentsShoppingList, B2bComponentsShoppingListEndpoint
from .commercial.b2b_components_shopping_list_line_item import (
    B2bComponentsShoppingListLineItem,
    B2bComponentsShoppingListLineItemEndpoint,
)
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
from .core.shipping_method_price import ShippingMethodPrice, ShippingMethodPriceEndpoint
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
    "B2bComponentsShoppingList",
    "B2bComponentsShoppingListLineItem",
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
    "ShippingMethodPrice",
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
    _custom_entities_loaded = False

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        from ...client import AdminClient
        assert isinstance(self, AdminClient)

        # Commercial
        self.b2b_employee = B2bEmployeeEndpoint(self)
        self.b2b_components_role = B2bComponentsRoleEndpoint(self)
        self.dynamic_access = DynamicAccessEndpoint(self)
        self.b2b_components_shopping_list = B2bComponentsShoppingListEndpoint(self)
        self.b2b_components_shopping_list_line_item = B2bComponentsShoppingListLineItemEndpoint(self)

        # Core
        self.acl_role = AclRoleEndpoint(self)
        self.api_info = ApiInfoEndpoint(self)
        self.app = AppEndpoint(self)
        self.app_script_condition = AppScriptConditionEndpoint(self)
        self.category = CategoryEndpoint(self)
        self.cms_block = CmsBlockEndpoint(self)
        self.cms_page = CmsPageEndpoint(self)
        self.cms_section = CmsSectionEndpoint(self)
        self.cms_slot = CmsSlotEndpoint(self)
        self.country = CountryEndpoint(self)
        self.country_state = CountryStateEndpoint(self)
        self.currency = CurrencyEndpoint(self)
        self.currency_country_rounding = CurrencyCountryRoundingEndpoint(self)
        self.custom_entity = CustomEntityEndpoint(self)
        self.custom_field = CustomFieldEndpoint(self)
        self.customer = CustomerEndpoint(self)
        self.customer_address = CustomerAddressEndpoint(self)
        self.customer_group = CustomerGroupEndpoint(self)
        self.customer_recovery = CustomerRecoveryEndpoint(self)
        self.customer_wishlist = CustomerWishlistEndpoint(self)
        self.customer_wishlist_product = CustomerWishlistProductEndpoint(self)
        self.delivery_time = DeliveryTimeEndpoint(self)
        self.document = DocumentEndpoint(self)
        self.document_base_config = DocumentBaseConfigEndpoint(self)
        self.document_base_config_sales_channel = DocumentBaseConfigSalesChannelEndpoint(self)
        self.document_type = DocumentTypeEndpoint(self)
        self.integration = IntegrationEndpoint(self)
        self.landing_page = LandingPageEndpoint(self)
        self.language = LanguageEndpoint(self)
        self.locale = LocaleEndpoint(self)
        self.main_category = MainCategoryEndpoint(self)
        self.media = MediaEndpoint(self)
        self.media_default_folder = MediaDefaultFolderEndpoint(self)
        self.media_folder = MediaFolderEndpoint(self)
        self.media_folder_configuration = MediaFolderConfigurationEndpoint(self)
        self.media_thumbnail = MediaThumbnailEndpoint(self)
        self.media_thumbnail_size = MediaThumbnailSizeEndpoint(self)
        self.order = OrderEndpoint(self)
        self.order_address = OrderAddressEndpoint(self)
        self.order_customer = OrderCustomerEndpoint(self)
        self.order_delivery = OrderDeliveryEndpoint(self)
        self.order_delivery_position = OrderDeliveryPositionEndpoint(self)
        self.order_line_item = OrderLineItemEndpoint(self)
        self.order_line_item_download = OrderLineItemDownloadEndpoint(self)
        self.order_transaction = OrderTransactionEndpoint(self)
        self.order_transaction_capture = OrderTransactionCaptureEndpoint(self)
        self.order_transaction_capture_refund = OrderTransactionCaptureRefundEndpoint(self)
        self.order_transaction_capture_refund_position = OrderTransactionCaptureRefundPositionEndpoint(self)
        self.payment_method = PaymentMethodEndpoint(self)
        self.product = ProductEndpoint(self)
        self.product_configurator_setting = ProductConfiguratorSettingEndpoint(self)
        self.product_cross_selling = ProductCrossSellingEndpoint(self)
        self.product_cross_selling_assigned_products = ProductCrossSellingAssignedProductsEndpoint(self)
        self.product_download = ProductDownloadEndpoint(self)
        self.product_export = ProductExportEndpoint(self)
        self.product_feature_set = ProductFeatureSetEndpoint(self)
        self.product_manufacturer = ProductManufacturerEndpoint(self)
        self.product_media = ProductMediaEndpoint(self)
        self.product_price = ProductPriceEndpoint(self)
        self.product_review = ProductReviewEndpoint(self)
        self.product_search_keyword = ProductSearchKeywordEndpoint(self)
        self.product_stream = ProductStreamEndpoint(self)
        self.product_visibility = ProductVisibilityEndpoint(self)
        self.product_warehouse = ProductWarehouseEndpoint(self)
        self.promotion = PromotionEndpoint(self)
        self.promotion_discount = PromotionDiscountEndpoint(self)
        self.promotion_discount_prices = PromotionDiscountPricesEndpoint(self)
        self.property_group = PropertyGroupEndpoint(self)
        self.property_group_option = PropertyGroupOptionEndpoint(self)
        self.rule = RuleEndpoint(self)
        self.rule_condition = RuleConditionEndpoint(self)
        self.sales_channel = SalesChannelEndpoint(self)
        self.sales_channel_domain = SalesChannelDomainEndpoint(self)
        self.salutation = SalutationEndpoint(self)
        self.seo_url = SeoUrlEndpoint(self)
        self.shipping_method = ShippingMethodEndpoint(self)
        self.shipping_method_price = ShippingMethodPriceEndpoint(self)
        self.state_machine = StateMachineEndpoint(self)
        self.state_machine_history = StateMachineHistoryEndpoint(self)
        self.state_machine_state = StateMachineStateEndpoint(self)
        self.state_machine_transition = StateMachineTransitionEndpoint(self)
        self.system_config = SystemConfigEndpoint(self)
        self.tag = TagEndpoint(self)
        self.tax = TaxEndpoint(self)
        self.tax_rule = TaxRuleEndpoint(self)
        self.tax_rule_type = TaxRuleTypeEndpoint(self)
        self.unit = UnitEndpoint(self)
        self.user = UserEndpoint(self)
        self.warehouse = WarehouseEndpoint(self)
        self.warehouse_group = WarehouseGroupEndpoint(self)
        self.warehouse_group_warehouse = WarehouseGroupWarehouseEndpoint(self)

        super().__init__(*args, **kwargs)

    @property
    def custom_entities_loaded(self) -> bool:
        return self._custom_entities_loaded

    async def load_custom_entities(self, client: "AdminClient | None" = None) -> None:
        if client is not None:
            import warnings
            warnings.warn("parameter 'client' of 'load_custom_entities' isn't used anymore and could get "
                          "removed in future versions.", DeprecationWarning)

        from ...client import AdminClient
        assert isinstance(self, AdminClient)

        if self.custom_entities_loaded:
            return

        from types import new_class

        from pydantic import AwareDatetime, create_model

        from ...base import AdminEndpoint
        from ..base_fields import IdField

        async for custom_entity in self.custom_entity.iter():
            assert isinstance(custom_entity, CustomEntity)
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
                        field_type = list[dict[str, Any]]
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

            ce_model: type[AdminModel[Any]] = create_model(
                custom_entity.name, **fields, __base__=AdminModel[AdminEndpoint]
            )

            ce_endpoint = new_class(f"{custom_entity.name}Endpoint", (AdminEndpoint[AdminModel],))
            ce_endpoint.name = custom_entity.name  # type: ignore
            ce_endpoint.path = f"/{custom_entity.name.replace('_', '-')}"  # type: ignore
            ce_endpoint.model_class = ce_model  # type: ignore

            setattr(self, custom_entity.name, ce_endpoint(self))

        self._custom_entities_loaded = True
