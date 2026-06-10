from fastapi import Request
from schemas.app_config import AppConfigModel
from services.runtime_config_service import RuntimeConfigService


def get_app_config(request: Request) -> AppConfigModel:
    deps = request.app.state.dependencies
    return deps["app_config"]


def get_runtime_config_service(request: Request) -> RuntimeConfigService:
    deps = request.app.state.dependencies
    return deps["runtime_config_service"]
