from typing import Optional
from bson import Binary
from pydantic import BaseModel
from decimal import Decimal
from enum import Enum

class PaymentMethod(str, Enum):

    Pix = "Pix"
    CreditCard = "Credit Card"
    DebitCard = "Debit Card"
    Money = "Money"

class Transaction(BaseModel):

    CodCli: int
    Cpf: Optional[str]
    Name: str
    Price: float
    Company: str
    PaymentMethod: str
    Product: str
