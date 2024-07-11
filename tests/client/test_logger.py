import unittest
from logging import Logger


class TestCRMLoggerAccess(unittest.TestCase):
    def test_logger_attr(self):
        self.assertTrue(hasattr(self._sut, "_logger"))
        self.assertTrue(hasattr(self._sut, "logger"))

    def test_logger_value(self):
        self.assertTrue(self._sut._logger, self._sut.logger)
        self.assertTrue(isinstance(self._sut.logger, Logger))

    def setUp(self):
        from app.client.base import SimpleAPIClient

        self._client = SimpleAPIClient()
        self._sut = self._client

    def _execute_sut(self, method, endpoint, data):
        return self._sut(method=method, endpoint=endpoint, data=data)
