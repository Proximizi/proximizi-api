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
async def get_proximies():
    return {"list of proximizes": proximizes}


@app.post("/proximies/")
async def create_proximie(new_proximize: Proximize):
    return new_proximize


@app.get("/proximizes/{id}")
async def get_proximie(proximize_id: int):
    return {"proximie_id": proximize_id}
