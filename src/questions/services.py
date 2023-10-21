from sqlalchemy import select
from src.questions.db_models import Question
from src.utils import get_async_api_data
from src.questions.schemas import QuestionAPIResponse, QuestionCreate
from src.database import db_manager

QUESTIONS_API_URL = 'https://jservice.io/api/random?count='


def get_questions_request_url(questions_num: int) -> str:
    request_url = f'{QUESTIONS_API_URL}{questions_num}'
    return request_url


async def get_questions(questions_num: int) -> list[QuestionAPIResponse]:
    request = get_questions_request_url(questions_num)
    api_data = await get_async_api_data(request)
    questions = [QuestionAPIResponse(**question) for question in api_data]
    return questions


async def create_new_questions(questions_num: int = None):
    if questions_num:
        questions_from_api = await get_questions(questions_num)
        questions = {
            question.question_id: QuestionCreate(**question.model_dump())
            for question in questions_from_api}
        question_ids = questions.keys()
        query_exist_ids = (select(Question)
                           .where(Question.question_id.in_(question_ids)))
        existing_questions_ids = await (db_manager.
                                        fetch_all_from_core(query_exist_ids))
        unique_questions_ids = (set(question_ids).
                                union(set(existing_questions_ids)))
        questions_for_add = [
            Question(**questions[k].model_dump())
            for k in unique_questions_ids if k in unique_questions_ids]
        await db_manager.insert_many_from_orm(questions_for_add)
        return create_new_questions(len(existing_questions_ids))
    return
