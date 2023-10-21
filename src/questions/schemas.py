from pydantic import BaseModel, Field
from datetime import datetime


class QuestionsNumber(BaseModel):
    questions_num: int = Field(
        title="The number of questions for adding", ge=1,
        examples=[1])


class BaseQuestion(BaseModel):
    question: str


class QuestionAPIResponse(BaseQuestion):
    question_id: int = Field(alias="id")
    answer: str
    question_created_at: datetime = Field(alias="created_at", parse_raw=True)

    class Config:
        populate_by_name = True


class QuestionCreate(QuestionAPIResponse):
    pass


class LatestQuestion(BaseQuestion):
    question: str = None
    created_at: datetime
