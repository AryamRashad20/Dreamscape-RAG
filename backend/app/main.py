from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.routes.query import router as query_router


app = FastAPI(
    title="Dreamscape RAG API",
    version="1.0.0",
    description="A RAG-powered assistant for the Dreamscape fantasy world."
)


# Allow the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Dreamscape RAG API"
    }


app.include_router(
    query_router,
    prefix="/api"
)