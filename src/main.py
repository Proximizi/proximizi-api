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
async def get_proximie(proximie_id: int):
    return {"proximie_id": proximie_id}
