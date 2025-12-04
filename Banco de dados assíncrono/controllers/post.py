from fastapi import status, APIRouter
from schemas.post import PostIn, PatchIn
from views.post import PostOut
from models.posts import posts
from database import database

router = APIRouter(prefix="/posts")

@router.get("/", response_model=list[PostOut])  #Query parameter
async def read_posts(published: bool, limit: int, skip: int = 0):
    query = posts.select()
    return await database.fetch_all(query)

@router.get("/{id}", response_model=PostOut)
async def read_post(id: int):
    query = posts.select().where(posts.c.id == id)
    return await database.fetch_one(query)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut) #Body parameter
async def create_post(post: PostIn):
    query = posts.insert().values(title=post.title, 
                                  content=post.content, 
                                  published_at=post.published_at,
                                  published=post.published)
    last_id = await database.execute(query)
    return {**post.model_dump(), "id":last_id}


@router.patch("/", response_model=PostOut)
async def update_post(new_content: PatchIn):
    query = posts.update().where(posts.c.id == new_content.id).values(content = new_content.content)
    await database.execute(query)
    return await database.fetch_one(posts.select().where(posts.c.id == new_content.id))

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_post(id: int = None, title: str = None):
    query = posts.delete().where(posts.c.id == id)
    await database.execute(query)
    return "Post deletado!"
