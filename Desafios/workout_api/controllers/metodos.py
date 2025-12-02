from fastapi import status, APIRouter, HTTPException
from schemas.entradas import PostIn
from views.retorno import PostOut

router = APIRouter(prefix="/workout")

fake_db = [{"id": 123, 
            "nome": "Mohamed Ali", 
            "cpf": "123.456.789-09", 
            "idade": 45, 
            "peso": 87, 
            "altura": 1.89,
            "sexo": "M",
            "centro_treinamento": 1,
            "categoria": 1}]

@router.post("/atletas", status_code=status.HTTP_201_CREATED, response_model=PostOut, summary="criar atleta",
    description="Endpoint responsável por criar um novo item no sistema.")
def criar_atleta(atleta: PostIn):
    atleta = atleta.model_dump()
    for i in fake_db:
        if i["cpf"] == atleta["cpf"]:
            raise HTTPException(
                status_code=409,
                detail=f"Usuário com o cpf: {atleta["cpf"]} já existe."
            )
    fake_db.append(atleta)
    return atleta

@router.get("/atletas/{nome}", response_model=list[PostOut], summary="filtrar atletas",
    description="Endpoint responsável por retornar atletas específicos, pelo nome ou CPF.")
def filtragem(limit: int, parametro: str, skip: int = 0):
    return [atleta for atleta in fake_db[skip: skip + limit] if atleta["nome"] == parametro or atleta["cpf"] == parametro]

@router.get("/atletas", response_model=list[PostOut], summary="retorna todos os atletas",
    description="Endpoint responsável por retornar todos os atletas cadastrados.")
def read_all():
    atletas = []
    for atleta in fake_db:
        atleta_novo = {"nome": atleta["nome"], 
                       "centro_treinamento": atleta["centro_treinamento"], 
                       "categoria": atleta["categoria"]}
        atletas.append(atleta_novo)
    return atletas
