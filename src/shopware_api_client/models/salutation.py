from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class SalutationBase(ApiModelBase, CustomFieldsMixin):
    _identifier = "salutation"

    salutation_key: str
    display_name: str
    letter_name: str
