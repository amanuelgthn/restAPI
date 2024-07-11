import unittest


class TestCRMClientInit(unittest.TestCase):
    def test_crm_client_init(self):
        from app.client.crm import CRMApiClient

        client = self._execute_sut("testing123", "https://example.com/unittest")

        self.assertIsInstance(client, CRMApiClient)
        self.assertEqual(client.api_key, "testing123")
        self.assertEqual(client.root_api_url, "https://example.com/unittest")

    def setUp(self):
        from app.client.crm import CRMApiClient

        self._sut = CRMApiClient

    def _execute_sut(self, api_key, root_api_url):
        return self._sut(api_key, root_api_url)
