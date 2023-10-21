from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import CursorResult, Select, Insert, Update, Any
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import MetaData
from src.config import settings

DATABASE_URL = settings.pgdb_url

Base = declarative_base()
metadata = MetaData()


class DatabaseManger:
    def __init__(self, db_url: str, echo: bool = False):
        self.async_engine = create_async_engine(
            url=db_url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.async_engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    """Methods for queries on sqlalchemy core level"""

    async def fetch_one_from_core(
            self,
            select_query: Select | Insert | Update) -> dict[str, Any] | None:
        async with self.async_engine.begin() as conn:
            cursor: CursorResult = await conn.execute(select_query)
            return cursor.first()._asdict() if cursor.rowcount > 0 else None

    async def fetch_all_from_core(
            self,
            select_query: Select | Insert | Update) -> list[dict[str, Any]]:
        async with self.async_engine.begin() as conn:
            cursor: CursorResult = await conn.execute(select_query)
            return [r._asdict() for r in cursor.all()]

    async def execute_from_core(self, select_query: Insert | Update) -> None:
        async with self.async_engine.begin() as conn:
            await conn.execute(select_query)

    """Methods for queries on sqlalchemy orm level"""

    async def get_session(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session

    async def insert_many_from_orm(self, rows: list[dict[str, Any]]) -> None:
        async with self.session_factory.begin() as session:
            session.add_all(rows)
            await session.commit()


db_manager = DatabaseManger(DATABASE_URL)
