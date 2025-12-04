from sqlmodel import SQLModel

class TransactionsReadIn(SQLModel):
    type: str | None = None