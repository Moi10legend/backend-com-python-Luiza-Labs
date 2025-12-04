from sqlmodel import SQLModel
from decimal import Decimal
from datetime import datetime

class TransactionReadOut(SQLModel):
    id: int
    value: Decimal
    type: str
    date: datetime