from app.models.deal import Deal
from app.models.user import User


DEALS_FAKE_RESPONSE = [
    {
        "id": "deal0001",
        "created": "2021-07-27T16:02:08.070557",
        "user_id": "user0002",
        "value": "129.99",
        "status": "pending",
    },
    {
        "id": "deal0002",
        "created": "2021-07-28T13:03:02.012333",
        "user_id": "user0001",
        "value": "13.29",
        "status": "success",
    },
    {
        "id": "deal0003",
        "created": "2021-07-28T14:04:08.073222",
        "user_id": "user0002",
        "value": "9.99",
        "status": "rejected",
    },
]

USERS_FAKE_RESPONSE = [
    {"id": "user0001", "name": "John Doe", "email": "johndoe@devskillers.com"},
    {"id": "user0002", "name": "Jane Doe", "email": "janedoe@devskillers.com"},
]


def dict_to_deal(data):
    return Deal(
        id=data["id"],
        created=data["created"],
        user_id=data["user_id"],
        value=data["value"],
        _status=data["status"],
    )


def dict_to_user(data):
    return User(id=data["id"], name=data["name"], email=data["email"])
