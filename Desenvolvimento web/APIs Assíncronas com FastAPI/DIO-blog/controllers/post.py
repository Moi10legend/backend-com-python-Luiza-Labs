from typing import Union, Annotated
from fastapi import status, Cookie, Response, Header, APIRouter
from datetime import datetime, UTC
from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix="/posts")

fake_db = [{"título": f"Criando uma aplicação com Django", "data": datetime.now(UTC), "publicado": True}, 
           {"título": f"Internacionalizando uma app Flask", "data": datetime.now(UTC), "publicado": True},
           {"título": f"Mais um React", "data": datetime.now(UTC), "publicado": True}]

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut) #Body parameter
def create_post(post: PostIn):
    fake_db.append(post.model_dump()) #model dump retorna a representação da classe em um dicionário
    return post

@router.get("/", response_model=list[PostOut])  #Query parameter
def read_posts(response: Response, 
               publicado: bool, 
               limit: int, 
               skip: int = 0, 
               ads_id: Annotated[str | None, Cookie()] = None,
               user_agent: Annotated[str | None, Header()] = None 
               ):
    
    response.set_cookie(key="user", value="efiwfio@gmail.com") #Setando um cookie
    print(f"User-agent: {user_agent}") #Lendo um header
    print(f"Cookies: {ads_id}")  #Lendo um cookie
    return [post for post in fake_db[skip: skip + limit] if post["publicado"] is publicado]

    
    
    # posts = []
    # for post in fake_db:
    #     if len(posts) == limit:
    #         break
    #     if post["publicado"] is publicado:
    #         posts.append(post)

    # return posts

@router.get("/{framework}", response_model=list[PostOut])  #Recebendo um atributo via path
def read_framework_posts(framework: str):
    return {"Posts": [{"título": f"Criando uma aplicação com {framework}", "data": datetime.now(UTC)}, 
                      {"título": f"Internacionalizando uma app {framework}"},
                      {"título": f"Mais um {framework}"}]}