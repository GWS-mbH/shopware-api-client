from typing import Any

from pydantic import Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField


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
    main_module: dict[str, Any] | None = None
    cookies: list[dict[str, Any]] | None = None
    allow_disable: bool
    base_app_url: str | None = None
    allowed_hosts: list[str] | None = None
    template_load_priority: int | None = None
    label: str
    description: str | None = None
    privacy_policy_extensions: str | None = None
    custom_fields: dict[str, Any] | None = None
    integration_id: IdField
    acl_role_id: IdField
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


class App(AppBase["AppEndpoint"], AppRelations):
    pass


class AppEndpoint(EndpointBase[App]):
    name = "app"
    path = "/app"
    model_class = App
