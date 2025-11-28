from pydantic import BaseModel

class PostOut(BaseModel):
    nome: str
    centro_treinamento: int
    categoria: int