from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

proximizes = []


class Proximize(BaseModel):
    name: str
    description: str


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/proximizes/")
async def get_proximizes():
    return {"list of proximizes": proximizes}


@app.post("/proximizes/")
async def create_proximize(new_proximize: Proximize):
    return new_proximize


@app.get("/proximizes/{id}")
async def get_proximize(proximize_id: int):
    return {"proximize_id": proximize_id}
