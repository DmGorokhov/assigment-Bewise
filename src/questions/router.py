from fastapi import APIRouter, Depends, status, Response
from fastapi.responses import JSONResponse
from .schemas import QuestionsNumber, LatestQuestion
from .dependencies import get_last_question
from fastapi.encoders import jsonable_encoder
from .services import create_new_questions

router = APIRouter(
    prefix="/questions",
    tags=["questions"],
    responses={404: {"description": "Not found"}},
)


@router.post("/add", status_code=status.HTTP_202_ACCEPTED)
async def add_new_questions(questions_to_add: QuestionsNumber,
                            last_question=Depends(
                                get_last_question)) -> Response:
    response_message = 'Last saved question'
    await create_new_questions(questions_to_add.questions_num)
    return JSONResponse(content={
        response_message: jsonable_encoder(LatestQuestion(**last_question)
                                           if last_question
                                           else "no questions in storage yet")})
