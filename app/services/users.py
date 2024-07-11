import typing

from .base import BaseCRMService
from ..models.user import User


class CRMUsersService(BaseCRMService):
    def get(self, user_id: str) -> typing.Optional[User]:
        json_response = self.client.call("GET", f"users/{user_id}")
        return (
            None
            if not json_response
            else User(
                id=json_response["id"],
                name=json_response["name"],
                email=json_response["email"],
            )
        )

    def get_list(self) -> typing.List[User]:
        json_response = self.client.call("GET", "users")
        return (
            []
            if not json_response
            else [
                User(id=row["id"], name=row["name"], email=row["email"])
                for row in json_response
            ]
        )
