from datetime import UTC, datetime

from shopware_api_client.endpoints.admin import MediaThumbnail


class TestThumbnail:
    def test_thumbnail_created_at_can_be_empty(self):
        thumbnail = MediaThumbnail(
            media_id="deadbeef123412341234123456789012",
            width=100,
            height=100,
            created_at=None,
            updated_at=None,
        )
        assert thumbnail.created_at is None
        assert thumbnail.updated_at is None

    def test_thumbnail_created_at_can_be_filled(self):
        thumbnail = MediaThumbnail(
            media_id="deadbeef123412341234123456789012",
            width=100,
            height=100,
            created_at="2023-01-01T00:00:00Z",
            updated_at=None,
        )
        assert thumbnail.created_at == datetime(2023, 1, 1, 0, 0, 0, tzinfo=UTC)
        assert thumbnail.updated_at is None
