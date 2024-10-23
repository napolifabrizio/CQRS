from pydantic import BaseModel
from decimal import Decimal
from enum import Enum

class PaymentMethod(str, Enum):

    Pix = "Pix"
    CreditCard = "Credit Card"
    DebitCard = "Debit Card"
    Money = "Money"

    @classmethod
    def is_valid(cls, method: str) -> bool:
        return method in cls._member_map

class Transaction(BaseModel):

    id: int
    Name: str
    Price: Decimal
    Company: str
    PaymentMethod: PaymentMethod
