from fastapi import FastAPI
from app.db.session import engine
from app.models.user import SQLModel
from app.api import auth, users

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI(title="FastAPI SQLModel Auth Example")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth.router, tags=["auth"])
app.include_router(users.router, tags=["users"])
