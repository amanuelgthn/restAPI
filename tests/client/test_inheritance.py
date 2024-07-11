import unittest


class TestCRMClientInheritance(unittest.TestCase):
    def test_crm_client_inherits_from_simple_api_client(self):
        from app.client.base import SimpleAPIClient

        self.assertTrue(issubclass(self._sut, SimpleAPIClient))

    def setUp(self):
        from app.client.crm import CRMApiClient

        self._sut = CRMApiClient
