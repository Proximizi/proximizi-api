from fastapi import FastAPI

app = FastAPI()

proximies = []


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/proximies/")
async def get_proximies():
    return {"list of proximies": proximies}


@app.get("/proximies/{id}")
async def get_proximie(id: int):
    return {"proximie_id": id}
