from sqlmodel import SQLModel

class TransactionsReadIn(SQLModel):
    account_id: int
    type: str | None = None