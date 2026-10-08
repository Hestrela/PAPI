from database.connection import init_db
from fastapi import FastAPI
from routers import projects, games, books
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World!"}

app.include_router(projects.router)
app.include_router(games.router)
app.include_router(books.router)