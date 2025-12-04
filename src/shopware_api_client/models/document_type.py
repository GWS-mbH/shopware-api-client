from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class DocumentTypeBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "document_type"

    name: str
    technical_name: str
