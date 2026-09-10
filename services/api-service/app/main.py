from fastapi import FastAPI

app = FastAPI(
    title="DistriRAG API Service",
    version="0.1.0",
    description="Event-driven document ingestion and vector query API",
)


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "api-service"}


@app.get("/")
async def root():
    return {"message": "Welcome to DistriRAG API Service"}
