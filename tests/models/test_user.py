import unittest
from dataclasses import asdict


class TestUserModel(unittest.TestCase):
    def test_asdict(self):
        self.assertDictEqual(
            asdict(self._user),
            {
                "id": "user0001",
                "name": "John Doe",
                "email": "johndoe@devskillers.com",
            },
        )

    def setUp(self):
        from app.models.user import User

        self._user = User(
            id="user0001",
            name="John Doe",
            email="johndoe@devskillers.com",
        )
