import datetime
import unittest
from dataclasses import asdict


class TestDealModel(unittest.TestCase):
    def test_is_success(self):
        from app.models.deal import DealStatus

        self._deal._status = DealStatus.SUCCESS
        self.assertTrue(self._deal.is_success())

    def test_is_rejected(self):
        from app.models.deal import DealStatus

        self._deal._status = DealStatus.REJECTED
        self.assertTrue(self._deal.is_rejected())

    def test_other_status(self):
        from app.models.deal import DealStatus

        self._deal._status = DealStatus.PENDING
        self.assertFalse(self._deal.is_success())
        self.assertFalse(self._deal.is_rejected())

    def test_asdict(self):
        self.assertDictEqual(
            asdict(self._deal),
            {
                "created": self._deal.created,
                "id": "deal0001",
                "user_id": "user0002",
                "value": "129.99",
                "_status": None,
            },
        )

    def setUp(self):
        from app.models.deal import Deal

        self._deal = Deal(
            created=datetime.datetime.now(),
            id="deal0001",
            user_id="user0002",
            value="129.99",
            _status=None,
        )
