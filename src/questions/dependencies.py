from sqlalchemy import select
from .db_models import Question
from src.database import db_manager


async def get_last_question() -> dict:
    select_query = select(Question).order_by(Question.created_at.desc()).limit(1) # noqa E501
    return await db_manager.fetch_one_from_core(select_query)
