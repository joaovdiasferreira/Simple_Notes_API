from fastapi import FastAPI
from app.routes import router
from database.connection import db_init
app = FastAPI(title="Simple Notes API", version="1.0.0")


app.include_router(router)