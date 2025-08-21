from fastapi import FastAPI
from route import router
import gc
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://zakariagoumri.vercel.app/chat"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
@app.head("/")
def root():
    return {"message": "server is running"}


@app.middleware("http")
async def cleanup_middleware(request, call_next):
    """Clean up memory after each request"""
    response = await call_next(request)
    gc.collect()
    return response
