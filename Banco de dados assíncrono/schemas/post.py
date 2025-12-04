from pydantic import BaseModel
from datetime import datetime, UTC

class PostIn(BaseModel):
    title: str
    content: str
    published_at: datetime | None = None
    published: bool=False

class PatchIn(BaseModel):
    id: int
    content: str