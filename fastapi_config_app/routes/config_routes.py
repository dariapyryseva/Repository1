from dependencies import get_app_config, get_runtime_config_service
from fastapi import APIRouter, Depends
from schemas.app_config import AppConfigModel
from schemas.responses import HealthResponse
from schemas.runtime_config import RuntimeConfigModel, RuntimeConfigUpdateModel
from services.runtime_config_service import RuntimeConfigService

router = APIRouter(tags=["configuration"])


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@router.get("/config/app", response_model=AppConfigModel)
def get_app_config_endpoint(config: AppConfigModel = Depends(get_app_config)):
    return config


@router.get("/config/runtime", response_model=RuntimeConfigModel)
def get_runtime_config(
    service: RuntimeConfigService = Depends(get_runtime_config_service),
):
    return service.get_config()


@router.put("/config/runtime", response_model=RuntimeConfigModel)
def update_runtime_config(
    update_data: RuntimeConfigUpdateModel,
    service: RuntimeConfigService = Depends(get_runtime_config_service),
):
    return service.update_config(update_data)
