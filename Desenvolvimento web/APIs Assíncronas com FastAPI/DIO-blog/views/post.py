from pydantic import BaseModel
from datetime import datetime

class PostOut(BaseModel):
    título: str
    data: datetime
    