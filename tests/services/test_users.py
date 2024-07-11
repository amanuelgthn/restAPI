import unittest
from unittest import mock

import requests_mock

from .base import USERS_FAKE_RESPONSE, dict_to_user


class TestCRMUsersService(unittest.TestCase):
    def test_list_response_type(self):
        from app.models.user import User
        from app.factory import api_crm_client_factory

        with requests_mock.Mocker() as m:
            m.get("https://example.com:1337/crm/v3/users", json=USERS_FAKE_RESPONSE)

            result = self._execute_sut(api_crm_client_factory).get_list()
            self.assertIsInstance(result, list)
            self.assertIsInstance(result[0], User)

    def test_list_client_mock(self):
        with requests_mock.Mocker() as m:
            m.get("https://example.com:1337/crm/v3/users", json=USERS_FAKE_RESPONSE)

            result = self._execute_sut(self._client_factory_mock).get_list()
            self.assertIsInstance(result, list)

    def test_list_response(self):
        from app.factory import api_crm_client_factory

        with requests_mock.Mocker() as m:
            m.get("https://example.com:1337/crm/v3/users", json=USERS_FAKE_RESPONSE)

            result = self._execute_sut(api_crm_client_factory).get_list()
            self.assertEqual(
                result, [dict_to_user(data) for data in USERS_FAKE_RESPONSE]
            )

    def test_get_response_type(self):
        from app.models.user import User
        from app.factory import api_crm_client_factory

        with requests_mock.Mocker() as m:
            m.get(
                f"https://example.com:1337/crm/v3/users/{        self._user_id}",
                json=USERS_FAKE_RESPONSE[0],
            )

            result = self._execute_sut(api_crm_client_factory).get(self._user_id)
            self.assertIsInstance(result, User)

    def test_get_response(self):
        from app.factory import api_crm_client_factory

        with requests_mock.Mocker() as m:
            m.get(
                f"https://example.com:1337/crm/v3/users/{self._user_id}",
                json=USERS_FAKE_RESPONSE[0],
            )

            result = self._execute_sut(api_crm_client_factory).get(self._user_id)
            expected_user = dict_to_user(USERS_FAKE_RESPONSE[0])
            self.assertEqual(result, expected_user)

    def test_get_client_mock(self):
        from app.models.user import User

        with requests_mock.Mocker() as m:
            m.get(
                f"https://example.com:1337/crm/v3/users/{self._user_id}",
                json=USERS_FAKE_RESPONSE[0],
            )

            result = self._execute_sut(self._client_factory_mock).get(self._user_id)
            self.assertIsInstance(result, User)

    def setUp(self):
        from app.services.users import CRMUsersService

        self._user_id = "user0001"
        self._sut = CRMUsersService

    def _execute_sut(self, client_factory):
        return self._sut(client_factory)

    def _client_factory_mock(self):
        return mock.MagicMock()
