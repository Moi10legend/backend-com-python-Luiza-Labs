from pydantic import BaseModel

class PostIn(BaseModel):
    nome: str
    cpf: str
    idade: int
    peso: float
    altura: float
    sexo: str
    centro_treinamento: int
    categoria: int