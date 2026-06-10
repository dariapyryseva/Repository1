from app.territories.router import router as territories_router
from fastapi import FastAPI

app = FastAPI(
    title="Urban Spatial Database API",
    description="CRUD-сервис для городских территорий и показателей",
    version="1.0.0",
)

app.include_router(territories_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
