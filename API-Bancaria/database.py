import sqlmodel as sm
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

sqlite_file_name = "database.db"
sqlite_url = f"sqlite+aiosqlite:///./{sqlite_file_name}"

engine = create_async_engine(
    sqlite_url,
    echo = True,
    future = True
)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

async def get_session():
    async with async_session() as session:
        yield session

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(sm.SQLModel.metadata.create_all)