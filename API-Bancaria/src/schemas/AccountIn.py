from sqlmodel import SQLModel

class AccountIn(SQLModel):
    name: str
    active: bool | None = None

