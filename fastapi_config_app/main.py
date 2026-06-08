from config import app_config
from fastapi import FastAPI
from routes.config_routes import router

app = FastAPI(
    title=app_config.app_name,
    version=app_config.app_version,
    description=app_config.app_description,
)

app.include_router(router)
