from sqlmodel import SQLModel
from decimal import Decimal

class TransactionCreate(SQLModel):
    account_id: int
    value: Decimal
    type: str