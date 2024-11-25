from fastapi import FastAPI
from domain.calendar import calendar_router

app = FastAPI()

app.include_router(calendar_router.router)

