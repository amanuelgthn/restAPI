import datetime
import decimal
from dataclasses import dataclass
from enum import Enum
from typing import List



class DealStatus(Enum):
    CREATED = "created"
    PENDING = "pending"
    REJECTED = "rejected"
    SUCCESS = "success"


@dataclass
class Deal:
    id: str
    created: datetime.datetime
    user_id: str
    value: decimal.Decimal
    _status: DealStatus

    def is_success(self) -> bool:
        return self._status == DealStatus.SUCCESS
    
    def is_rejected(self) -> bool:
        return self._status == DealStatus.REJECTED
    
    @classmethod
    def get_list(cls, deals):
        return [cls(**deal) for deal in deals]
    