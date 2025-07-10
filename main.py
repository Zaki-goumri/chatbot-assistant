from fastapi import FastAPI
from route import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def root():
    return {"message": "server is running"}
