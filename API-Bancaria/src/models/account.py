from sqlmodel import SQLModel, Field, Relationship
from decimal import Decimal
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .transaction import Transaction

class Account(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    password: str
    balance: Decimal | None = Field(default=0, decimal_places=2)
    active: bool | None = Field(default=True)
    transaction: list["Transaction"] = Relationship(back_populates="account", cascade_delete=True)