from shopware_api_client.models.property_group import PropertyGroup as PropertyGroupBase


class PropertyGroup(PropertyGroupBase):
    options: list["PropertyGroupOption"] | None = None


from .property_group_option import PropertyGroupOption  # noqa: E402
