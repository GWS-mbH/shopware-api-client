from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...relations import ManyRelation


class CustomerGroupBase(ApiModelBase[EndpointClass]):
    _identifier = "customer_group"

    name: str
    display_gross: bool | None = None
    custom_fields: dict[str, Any] | None = None
    registration_active: bool | None = None
    registration_title: str | None = None
    registration_introduction: str | None = None
    registration_only_company_registration: bool | None = None
    registration_seo_meta_description: str | None = None
    translated: dict[str, Any] | None = None


class CustomerGroupRelations:
    customers: ManyRelation["Customer"]
    sales_channels: ManyRelation["SalesChannel"]
    registration_sales_channels: ManyRelation["SalesChannel"]


class CustomerGroup(CustomerGroupBase["CustomerGroupEndpoint"], CustomerGroupRelations):
    pass


class CustomerGroupEndpoint(EndpointBase[CustomerGroup]):
    name = "customer_group"
    path = "/customer-group"
    model_class = CustomerGroup


from .customer import Customer  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
