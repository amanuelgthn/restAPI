import typing

from .base import BaseCRMService
from ..models.deal import Deal


class CRMDealsService(BaseCRMService):
    def get(self, deal_id: str) -> typing.Optional[Deal]:
        json_response = self.client.call("GET", f"deals/{deal_id}")
        return (
            None
            if not json_response
            else Deal(
                id=json_response["id"],
                created=json_response["created"],
                user_id=json_response["user_id"],
                value=json_response["value"],
                _status=json_response["status"],
            )
        )

    def get_list(self) -> typing.List[Deal]:
        json_response = self.client.call("GET", "deals")
        return [Deal(
            id=deal["id"],
            created=deal["created"],
            user_id=deal["user_id"],
            value=deal["value"],
            _status=deal["status"],
        ) for deal in json_response]
