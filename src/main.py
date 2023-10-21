from fastapi import FastAPI
from .config import app_configs, settings
from .questions.router import router as questions_router

app = FastAPI(**app_configs)

api_prefix = settings.API_V1_STR
app.include_router(questions_router, prefix=api_prefix)
