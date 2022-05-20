from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

proximies = []


class Proximie(BaseModel):
    name: str
    description: str


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/proximies/")
async def get_proximies():
    return {"list of proximies": proximies}


@app.post("/proximies/")
async def create_proximie(new_proximise: Proximie):
    return new_proximise


@app.get("/proximies/{id}")
async def get_proximie(proximie_id: int):
    return {"proximie_id": proximie_id}
