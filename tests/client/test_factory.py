import os
import unittest
from unittest import mock


class TestCRMClientFactory(unittest.TestCase):
    def test_dummy_client_testing_env(self):
        from app.client.dummy import DummyAPIClient

        with mock.patch.dict(os.environ, {"ENV": "testing"}):
            client = self._execute_sut()

            self.assertIsInstance(client, DummyAPIClient)

    def test_crm_client(self):
        from app.client.crm import CRMApiClient
        from app import settings

        old_api_key = settings.CRM_API_KEY
        old_api_url = settings.CRM_API_URL

        settings.CRM_API_KEY = "testing123"
        settings.CRM_API_URL = "https://example.com/unittest"

        with mock.patch.dict(
            os.environ,
        ):
            client = self._execute_sut()

            self.assertIsInstance(client, CRMApiClient)
            self.assertEqual(client.api_key, "testing123")
            self.assertEqual(client.root_api_url, "https://example.com/unittest")

        settings.CRM_API_KEY = old_api_key
        settings.CRM_API_URL = old_api_url

    def setUp(self):
        from app.factory import api_crm_client_factory

        self._sut = api_crm_client_factory

    def _execute_sut(self):
        return self._sut()
