from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["Home"])
async def home():
    return {"message": "Welcome to this fantastic app!"}
