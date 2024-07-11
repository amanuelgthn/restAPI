import os

from . import settings
from .client.base import SimpleAPIClient
from .client.crm import CRMApiClient
from .client.dummy import DummyAPIClient


def api_crm_client_factory() -> SimpleAPIClient:
    if os.environ.get("ENV") == "testing":
        return DummyAPIClient()
    return CRMApiClient(api_key=settings.CRM_API_KEY, root_api_url=settings.CRM_API_URL)
