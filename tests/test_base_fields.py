import json

import pytest
from pydantic import BaseModel

from shopware_api_client.endpoints.base_fields import IdField, PhpAssocArray


class TestModel(BaseModel):
    data: PhpAssocArray
    id: IdField | None = None


class TestBaseFields:
    @pytest.mark.parametrize(
        "input_value, expected_output",
        [
            ({"key": "value"}, {"key": "value"}),
            ([], {}),
            (None, None),
        ],
    )
    def test_php_assoc_array_valid(self, input_value, expected_output) -> None:
        model = TestModel(data=input_value)
        assert model.data == expected_output

        json_model = TestModel.model_validate_json(json.dumps({"data": input_value}))
        assert json_model.data == expected_output

    def test_php_assoc_array_invalid_list(self) -> None:
        with pytest.raises(ValueError) as exc_info:
            TestModel(data=[{"key": "value"}])
        assert "Expected an associative array, but got a non-empty list" in str(exc_info.value)

    def test_php_assoc_array_invalid_type(self) -> None:
        with pytest.raises(ValueError):
            TestModel(data="not a dict or list")  # type: ignore

    def test_idfield_valid(self) -> None:
        model = TestModel(data={}, id="1234567890abcdef1234567890abcdef")
        assert model.id == "1234567890abcdef1234567890abcdef"

    def test_idfield_invalid(self) -> None:
        with pytest.raises(ValueError) as exc_info:
            TestModel(data={}, id="invalid_id")
        assert "String should match pattern" in str(exc_info.value)

    def test_idfield_none(self) -> None:
        model = TestModel(data={}, id=None)
        assert model.id is None
