from fastapi import FastAPI
from route import router
import gc
import os

app = FastAPI()

# Optimize FastAPI memory usage
app.include_router(router)


@app.get("/")
def root():
    return {"message": "server is running"}


@app.middleware("http")
async def cleanup_middleware(request, call_next):
    """Clean up memory after each request"""
    response = await call_next(request)
    gc.collect()
    return response
