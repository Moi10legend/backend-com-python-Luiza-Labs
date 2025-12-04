from sqlmodel import SQLModel

class AccountIn(SQLModel):
    name: str
    password: str
    active: bool | None = None

