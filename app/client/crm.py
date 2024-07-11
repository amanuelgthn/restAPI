import logging
import typing
import requests
from .base import SimpleAPIClient

class CRMApiClient(SimpleAPIClient):
    _logger: logging.Logger = logging.getLogger("crm_client")
    
    def __init__(self, api_key: str, root_api_url: str):
        self.api_key = api_key
        self.root_api_url = root_api_url

    def call(
        self,
        method: str,
        endpoint: str,
        data: typing.Optional[dict] = None,
        **kwargs,
    ) -> dict:
        headers = {"Api-Token": self.api_key}
        return self._call(
            method=method,
            root_api_url=self.root_api_url,  # Added root_api_url here
            endpoint=endpoint,
            data=data,
            headers=headers,
            **kwargs
        )

    def _call(
        self,
        method: str,
        root_api_url: str,  # Added root_api_url parameter here
        endpoint: str,
        data: typing.Optional[dict] = None,
        headers: typing.Optional[dict] = None,
        **kwargs,
    ) -> dict:
        url = f"{root_api_url}{endpoint.lstrip('/')}"
        print("endpointapi {}".format(endpoint))
        self._logger.debug(f"Making request to {url} with method {method} and data {data}")
        response = requests.request(
            method=method,
            url=url,
            json=data,
            headers=headers,
            **kwargs,
        )
        self._check_response(response)
        return response.json()

    def _check_response(self, response: requests.Response) -> None:
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            self._logger.error(f"HTTPError occurred: {e}")
            raise
