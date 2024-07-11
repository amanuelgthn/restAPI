import abc
import json
import logging
import typing
from functools import cached_property
from urllib.parse import urljoin

from requests import Session, Response, adapters


class SimpleAPIClient:
    timeout: typing.Optional[int] = None
    max_retries: int = 3
    _logger: logging.Logger = logging.getLogger(__name__)

    @cached_property
    def session(self) -> Session:
        session = Session()
        adapter = adapters.HTTPAdapter(max_retries=self.max_retries)
        session.mount("https://", adapter)
        return session

    @abc.abstractmethod
    def call(
        self,
        method: str,
        endpoint: str,
        data: typing.Optional[dict] = None,
        **kwargs,
    ) -> dict:
        pass

    @abc.abstractmethod
    def _check_response(self, response: Response) -> None:
        pass

    def _call(
        self,
        method: str,
        root_api_url: str,
        endpoint: str,
        data: typing.Optional[dict] = None,
        headers: typing.Optional[dict] = None,
        **kwargs,
    ) -> dict:
        url = urljoin(root_api_url, endpoint)
        default_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        if headers:
            default_headers.update(headers)
        self.logger.debug(f"Request: {method} {url}")
        response = self.session.request(
            method,
            url,
            data=json.dumps(data or {}),
            params=kwargs,
            headers=default_headers,
            timeout=self.timeout,
        )
        self.logger.debug(f"Response: {response.text}")
        self._check_response(response)
        return response.json()
    
    @property
    def logger(self) -> logging.Logger:
        return self._logger
