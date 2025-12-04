from fastapi import FastAPI
from database import database, engine, metadata
from contextlib import asynccontextmanager
from controllers import post

@asynccontextmanager
async def lifespan(app: FastAPI):    
    from models.posts import posts  #noqa
    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(post.router)