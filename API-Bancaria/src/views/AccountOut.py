from sqlmodel import SQLModel
from decimal import Decimal

class AccountOut(SQLModel):
    id: int
    name: str
    balance: Decimal
    active: bool