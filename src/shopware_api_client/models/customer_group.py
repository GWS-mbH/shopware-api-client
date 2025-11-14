from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class CustomerGroupBase(ApiModelBase, CustomFieldsMixin):
    _identifier = "customer_group"

    name: str
    display_gross: bool | None = None
    registration_active: bool | None = None
    registration_title: str | None = None
    registration_introduction: str | None = None
    registration_only_company_registration: bool | None = None
    registration_seo_meta_description: str | None = None
