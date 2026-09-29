from fastapi import FastAPI
from routers import projects


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

app.include_router(projects.router)

