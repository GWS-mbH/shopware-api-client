from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField

if TYPE_CHECKING:
    pass


class AppBase(ApiModelBase[EndpointClass]):
    _identifier = "app"

    name: str
    path: str
    author: str | None = None
    copyright: str | None = None
    license: str | None = None
    active: bool
    configurable: bool
    privacy: str | None = None
    version: str
    icon: str | None = Field(None, description="Runtime field, cannot be used as part of the criteria.", exclude=True)
    modules: list[dict[str, Any]] | None = None
    main_module: dict[str, Any] | None = Field(
        default=None, serialization_alias="mainModule", validation_alias=AliasChoices("main_module", "mainModule")
    )
    cookies: list[dict[str, Any]] | None = None
    allow_disable: bool = Field(
        ..., serialization_alias="allowDisable", validation_alias=AliasChoices("allow_disable", "allowDisable")
    )
    base_app_url: str | None = Field(
        default=None, serialization_alias="baseAppUrl", validation_alias=AliasChoices("base_app_url", "baseAppUrl")
    )
    allowed_hosts: list[str] | None = Field(
        default=None, serialization_alias="allowedHosts", validation_alias=AliasChoices("allowed_hosts", "allowedHosts")
    )
    template_load_priority: int | None = Field(
        default=None,
        serialization_alias="templateLoadPriority",
        validation_alias=AliasChoices("template_load_priority", "templateLoadPriority"),
    )
    label: str
    description: str | None = None
    privacy_policy_extensions: str | None = Field(
        default=None,
        serialization_alias="privacyPolicyExtensions",
        validation_alias=AliasChoices("privacy_policy_extensions", "privacyPolicyExtensions"),
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    integration_id: IdField = Field(
        ..., serialization_alias="integrationId", validation_alias=AliasChoices("integration_id", "integrationId")
    )
    acl_role_id: IdField = Field(
        ..., serialization_alias="aclRoleId", validation_alias=AliasChoices("acl_role_id", "aclRoleId")
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
    translated: dict[str, Any] | None = None


class AppRelations:
    # integration: Integration | None = None
    # acl_role: AclRole | None = Field(None, alias="aclRole")
    # custom_field_sets: list[CustomFieldSet] | None = Field(
    #     None, alias="customFieldSets"
    # )
    # action_buttons: list[AppActionButton] | None = Field(None, alias="actionButtons")
    # templates: list[AppTemplate] | None = None
    # webhooks: list[Webhook] | None = None
    # payment_methods: list[AppPaymentMethod] | None = Field(None, alias="paymentMethods")
    # tax_providers: list[TaxProvider] | None = Field(None, alias="taxProviders")
    # cms_blocks: list[AppCmsBlock] | None = Field(None, alias="cmsBlocks")
    # flow_actions: list[AppFlowAction] | None = Field(None, alias="flowActions")
    # flow_events: list[AppFlowEvent] | None = Field(None, alias="flowEvents")
    # app_shipping_methods: list[AppShippingMethod] | None = Field(
    #     None, alias="appShippingMethods"
    # )
    pass


class App(AppBase["AppModelEndpoint"], AppRelations):
    pass


class AppModelEndpoint(EndpointBase[App]):
    name = "app"
    path = "/app"
    model_class = App


registry.register_admin(AppModelEndpoint)
