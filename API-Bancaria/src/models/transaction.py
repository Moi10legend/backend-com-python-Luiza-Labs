from sqlmodel import SQLModel, Field, Relationship
from decimal import Decimal
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .account import Account

class Transaction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    account_id: int = Field(foreign_key="account.id")
    value: Decimal = Field(decimal_places=2)
    type: str
    date: datetime | None = Field(default=datetime.now(ZoneInfo("America/Recife")))
    account: "Account" = Relationship(back_populates="transaction")