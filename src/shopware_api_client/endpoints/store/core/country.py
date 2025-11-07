from shopware_api_client.models.country import Country as CountryBase


class Country(CountryBase):
    states: list["CountryState"] | None = None


from .country_state import CountryState  # noqa: E402
