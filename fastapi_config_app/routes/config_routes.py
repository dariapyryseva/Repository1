from config import AppConfig, app_config, runtime_config
from fastapi import APIRouter
from services.runtime_service import (
    get_runtime_config,
    update_runtime_config,
)

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/config/app")
def get_app_config():
    return app_config


@router.get("/config/runtime")
def get_runtime():
    return get_runtime_config()


@router.put("/config/runtime")
def update_runtime(new_config: AppConfig):
    return update_runtime_config(new_config)
