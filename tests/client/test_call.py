import unittest
from unittest import mock


class TestCRMClientCall(unittest.TestCase):
    def test_parent_call_is_called(self):
        self._execute_sut("GET", "users", {"name": "ABC"})
        self._client._call.assert_called_once_with(
            method="GET",
            root_api_url="http://devskillers.com/api/v3/",
            endpoint="users",
            data={"name": "ABC"},
            headers={"Api-Token": "key123"},
        )

    def setUp(self):
        from app.client.crm import CRMApiClient

        self._client = CRMApiClient("key123", "http://devskillers.com/api/v3/")
        self._client._call = mock.Mock()
        self._sut = self._client.call

    def _execute_sut(self, method, endpoint, data):
        return self._sut(method=method, endpoint=endpoint, data=data)
