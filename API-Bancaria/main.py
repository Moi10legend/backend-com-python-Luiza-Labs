from fastapi import FastAPI
from database import create_db, engine
from contextlib import asynccontextmanager
from src.controllers import routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Isso força o carregamento das classes e o registro no metadata
    from src.models import Account, Transaction
    await create_db()
    yield
    await engine.dispose()

app = FastAPI(
    title="API Bancária",
    version= "1.0.0",
    lifespan=lifespan
)
app.include_router(routes.router)


