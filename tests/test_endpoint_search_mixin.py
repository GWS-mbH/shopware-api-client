"""
Tests the methods of the EndpointSearchMixin class.
Especially the filter and exclude methods, which are used to filter and exclude endpoints based on certain criteria.
"""

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin, EndpointSearchMixin


class TestModel(ApiModelBase, CustomFieldsMixin):
    """
    A test model class to be used in the tests.
    """

    _identifier: str = "test_model"

    name: str


class TestEndpointSearchMixin:
    """
    Tests the methods of the EndpointSearchMixin class.
    """

    def test_filter(self):
        """
        Tests the filter method of the EndpointSearchMixin class.
        """
        query = EndpointSearchMixin()
        query.model_class = TestModel
        query = query.filter(custom_fields__gws_erp_order_number__startswith="TEST1234", name="Test")
        output = query._get_data_dict()

        assert output == {
            "filter": [
                {
                    "field": "customFields.gws_erp_order_number",
                    "parameters": {},
                    "type": "prefix",
                    "value": "TEST1234",
                },
                {
                    "field": "name",
                    "parameters": {},
                    "type": "equals",
                    "value": "Test",
                },
            ]
        }

    def test_exclude(self):
        """
        Tests the exclude method of the EndpointSearchMixin class.
        """
        query = EndpointSearchMixin()
        query.model_class = TestModel
        query = query.exclude(custom_fields__gws_erp_order_number__startswith="TEST1234", name="Test")
        output = query._get_data_dict()

        assert output == {
            "filter": [
                {
                    "operator": "and",
                    "queries": [
                        {
                            "field": "customFields.gws_erp_order_number",
                            "parameters": {},
                            "type": "prefix",
                            "value": "TEST1234",
                        },
                        {
                            "field": "name",
                            "parameters": {},
                            "type": "equals",
                            "value": "Test",
                        },
                    ],
                    "type": "not",
                }
            ]
        }
