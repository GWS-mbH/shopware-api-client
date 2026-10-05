from pytest_mock import MockerFixture

from shopware_api_client.client import AdminClient
from shopware_api_client.config import AdminConfig
from shopware_api_client.endpoints.admin.core.currency import CurrencyEndpoint
from shopware_api_client.endpoints.admin.core.media import MediaEndpoint
from shopware_api_client.endpoints.admin.core.media_thumbnail import MediaThumbnail
from shopware_api_client.endpoints.admin.core.media_thumbnail_size import MediaThumbnailSizeEndpoint
from shopware_api_client.endpoints.admin.core.product import ProductEndpoint
from shopware_api_client.endpoints.admin.core.product_price import ProductPrice
from shopware_api_client.endpoints.admin.core.rule import RuleEndpoint
from shopware_api_client.structs.price import Price

PRODUCT_ID = "1" * 32
PRODUCT_VERSION_ID = "2" * 32
RULE_ID = "3" * 32
CURRENCY_ID = "4" * 32
LIST_PRICE_CURRENCY_ID = "5" * 32
MEDIA_ID = "6" * 32
UNKNOWN_ID = "7" * 32


class TestForeignKeys:
    def test__get_foreign_key_fields(self) -> None:
        result = ProductPrice.get_foreign_key_fields()

        assert "product_version_id" not in result, "version_ids are not FK and should not be included"
        assert result == {
            "product_id": ProductEndpoint,
            "rule_id": RuleEndpoint,
            "price.currency_id": CurrencyEndpoint,
            "product": ProductEndpoint,
            "rule": RuleEndpoint,
        }

    def test__get_fk_ids_by_endpoint(self) -> None:
        product_price = ProductPrice(
            product_id=PRODUCT_ID,
            product_version_id=PRODUCT_VERSION_ID,
            rule_id=RULE_ID,
            quantity_start=1,
            price=[
                Price(
                    currency_id=CURRENCY_ID,
                    gross=10.0,
                    net=8.4,
                    linked=False,
                    list_price=Price(currency_id=LIST_PRICE_CURRENCY_ID, gross=12.0, net=10.1, linked=False),
                )
            ],
        )

        assert product_price.get_fk_ids_by_endpoint() == {
            ProductEndpoint: {PRODUCT_ID},
            RuleEndpoint: {RULE_ID},
            CurrencyEndpoint: {CURRENCY_ID, LIST_PRICE_CURRENCY_ID},
        }

    def test__get_fk_ids_by_endpoint_with_unset_id_field(self) -> None:
        media_thumbnail = MediaThumbnail(media_id=MEDIA_ID)

        result = media_thumbnail.get_fk_ids_by_endpoint()

        assert MediaThumbnailSizeEndpoint not in result, "endpoints of unset id fields should not be included"
        assert result == {MediaEndpoint: {MEDIA_ID}}

    async def test__get_fk_ids_by_endpoint_custom_entity(self, mocker: MockerFixture) -> None:
        client = AdminClient(config=AdminConfig(url="https://localhost", client_id="ID", client_secret="SECRET"))
        custom_entity = client.custom_entity.model_class(
            name="my_fk_custom_entity",
            fields=[
                {"name": "media", "type": "many-to-one", "reference": "media", "required": True},
                {"name": "unknown", "type": "many-to-one", "reference": "not_an_entity", "required": True},
            ],
        )

        async def fake_iter():
            yield custom_entity

        mocker.patch.object(type(client.custom_entity), "iter", return_value=fake_iter())
        await client.load_custom_entities()

        custom_model = client.my_fk_custom_entity.model_class(media_id=MEDIA_ID, unknown_id=UNKNOWN_ID)

        result = custom_model.get_fk_ids_by_endpoint()

        assert not any(UNKNOWN_ID in ids for ids in result.values()), "entities without an endpoint should not be included"
        assert result == {MediaEndpoint: {MEDIA_ID}}
