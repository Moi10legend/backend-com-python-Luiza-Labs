from sqlmodel import SQLModel
from decimal import Decimal

class TransactionCreate(SQLModel):
    value: Decimal
    type: str