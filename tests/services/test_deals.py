import unittest
from unittest import mock

import requests_mock

from .base import DEALS_FAKE_RESPONSE, dict_to_deal


class TestCRMDealsService(unittest.TestCase):
    def test_list_response_type(self):
        from app.models.deal import Deal
        from app.factory import api_crm_client_factory

        with requests_mock.Mocker() as m:
            m.get("https://example.com:1337/crm/v3/deals", json=DEALS_FAKE_RESPONSE)
            result = self._execute_sut(api_crm_client_factory).get_list()
            self.assertIsInstance(result, list)
            self.assertIsInstance(result[0], Deal)

    def test_list_client_mock(self):
        with requests_mock.Mocker() as m:
            m.get("https://example.com:1337/crm/v3/deals", json=DEALS_FAKE_RESPONSE)
            result = self._execute_sut(self._client_factory_mock).get_list()
            self.assertIsInstance(result, list)

    def test_list_response(self):
        from app.factory import api_crm_client_factory

        with requests_mock.Mocker() as m:
            m.get("https://example.com:1337/crm/v3/deals", json=DEALS_FAKE_RESPONSE)

            result = self._execute_sut(api_crm_client_factory).get_list()
            self.assertEqual(
                result, [dict_to_deal(data) for data in DEALS_FAKE_RESPONSE]
            )

    def test_get_response_type(self):
        from app.models.deal import Deal
        from app.factory import api_crm_client_factory

        deal_id = "deal0002"
        with requests_mock.Mocker() as m:
            m.get(
                f"https://example.com:1337/crm/v3/deals/{deal_id}",
                json=DEALS_FAKE_RESPONSE[1],
            )
            deal = self._execute_sut(api_crm_client_factory).get(deal_id)
            self.assertIsInstance(deal, Deal)

    def test_get_response(self):
        from app.factory import api_crm_client_factory

        deal_id = "deal0002"
        with requests_mock.Mocker() as m:
            m.get(
                f"https://example.com:1337/crm/v3/deals/{deal_id}",
                json=DEALS_FAKE_RESPONSE[1],
            )

            deal = self._execute_sut(api_crm_client_factory).get(deal_id)
            expected_deal = dict_to_deal(DEALS_FAKE_RESPONSE[1])
            self.assertEqual(deal, expected_deal)

    def test_get_client_mock(self):
        from app.models.deal import Deal

        deal_id = "deal0002"
        with requests_mock.Mocker() as m:
            m.get(
                f"https://example.com:1337/crm/v3/deals/{deal_id}",
                json=DEALS_FAKE_RESPONSE[1],
            )

            deal = self._execute_sut(self._client_factory_mock).get(deal_id)
            self.assertIsInstance(deal, Deal)

    def setUp(self):
        from app.services.deals import CRMDealsService

        self._sut = CRMDealsService

    def _execute_sut(self, client_factory):
        return self._sut(client_factory)

    def _client_factory_mock(self):
        return mock.MagicMock()
