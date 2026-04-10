from fastapi import FastAPI
from app.routes import router
from database.connection import db_init

#starting app
app = FastAPI(title="Simple Notes API", version="1.0.0")

#getting routes from app/routes
app.include_router(router)