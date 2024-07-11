import logging
import typing
from functools import cached_property

import requests

from .base import SimpleAPIClient


class DummyAPIClient(SimpleAPIClient):
    _logger: logging.Logger = logging.getLogger("dummy_client")

    @cached_property
    def session(self) -> None:
        return None

    def call(
        self,
        method: str,
        endpoint: str,
        data: typing.Optional[dict] = None,
        **kwargs,
    ) -> None:
        self.logger.debug(f"FAKE Request: {method} {endpoint}")

    def _check_response(self, response: requests.Response) -> None:
        return None
