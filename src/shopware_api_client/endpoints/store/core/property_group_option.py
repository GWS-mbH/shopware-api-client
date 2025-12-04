from shopware_api_client.models.property_group_option import PropertyGroupOptionBase


class PropertyGroupOption(PropertyGroupOptionBase):
    media: "Media | None" = None
    group: "PropertyGroup"


from .media import Media  # noqa: E402
from .property_group import PropertyGroup  # noqa: E402
