import pytest
from httpx2 import Request, Response

from shopware_api_client.endpoints.admin import Unit
from shopware_api_client.exceptions import (
    SWAPIError,
    SWAPIErrorList,
    SWAPIInternalServerError,
    SWAPISqlDuplicateEntryError,
    SWAPISqlForeignKeyError,
)


class TestSWAPIError:
    orig_objs = [
        Unit(short_code="test_1", name="Test_1"),
        Unit(short_code="test_2", name="Test_2"),
        Unit(short_code="test_3", name="Test_3"),
    ]

    def test_from_errors_400s(self) -> None:
        errors = [
            {
                "status": "400",
                "code": "TESTCODE_1",
                "detail": "Test error occurred",
                "source": {"pointer": "/body/0/short_code"},
            },
            {
                "status": "400",
                "code": "TESTCODE_2",
                "detail": "Another test error occurred",
                "source": {"pointer": "/body/1/nested/attr"},
            },
            {
                "status": "400",
                "code": "TESTCODE_3",
                "detail": "Another test error occurred",
            },
        ]
        response = Response(
            status_code=400,
            json={"errors": errors},
            request=Request("POST", "https://test.com/api/unit"),
        )

        result = SWAPIError.from_errors(errors, response, self.orig_objs)

        assert isinstance(result, SWAPIErrorList)
        assert len(result.errors) == 3

        for i, error in enumerate(errors):
            for attr in "status", "code", "detail":
                assert getattr(result.errors[i], attr) == error[attr]

        assert result.errors[0].pointer_idx == 0
        assert result.errors[0].pointer_entity == "unit"
        assert result.errors[0].pointer_field == "short_code"
        assert result.errors[0].pointer_orig_obj == self.orig_objs[0]

        assert result.errors[1].pointer_idx == 1
        assert result.errors[1].pointer_entity == "unit"
        assert result.errors[1].pointer_field == "nested/attr"
        assert result.errors[1].pointer_orig_obj == self.orig_objs[1]

        assert result.errors[2].pointer_idx is None
        assert result.errors[2].pointer_entity is None
        assert result.errors[2].pointer_field is None
        assert result.errors[2].pointer_orig_obj is None

    @pytest.mark.parametrize(
        "errors, error_type",
        [
            (
                [
                    {
                        "status": "500",
                        "code": "TESTCODE_1",
                        "detail": "Test error occurred",
                    }
                ],
                SWAPIInternalServerError,
            ),
            (
                [
                    {
                        "status": "500",
                        "code": "1062",
                        "detail": "An exception occurred while executing a query: SQLSTATE[23000]: Duplicate Error: 1062 ...",
                    }
                ],
                SWAPISqlDuplicateEntryError,
            ),
            (
                [
                    {
                        "status": "500",
                        "code": "1452",
                        "detail": "An exception occurred while executing a query: SQLSTATE[23000]: Integrity constraint violation: 1452 ...",
                    }
                ],
                SWAPISqlForeignKeyError,
            ),
        ],
    )
    def test_from_errors_500s(self, errors: list[dict[str, str]], error_type: type[SWAPIInternalServerError]) -> None:
        response = Response(
            status_code=500,
            json={"errors": errors},
            request=Request("POST", "https://test.com/api/unit"),
        )

        result = SWAPIError.from_errors(errors, response, self.orig_objs)

        assert isinstance(result, SWAPIErrorList)
        assert len(result.errors) == 1
        assert isinstance(result.errors[0], error_type)

        assert result.errors[0].status == errors[0]["status"]
        assert result.errors[0].code == errors[0]["code"]
        assert result.errors[0].detail == errors[0]["detail"]

        assert result.errors[0].pointer_idx is None
        assert result.errors[0].pointer_entity is None
        assert result.errors[0].pointer_field is None
        assert result.errors[0].pointer_orig_obj is None
