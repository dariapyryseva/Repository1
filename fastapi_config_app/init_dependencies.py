from schemas.app_config import AppConfigModel
from schemas.runtime_config import RuntimeConfigModel
from services.runtime_config_service import RuntimeConfigService


def init_dependencies() -> dict:
    static_config = AppConfigModel(
        app_name="Laboratory FastAPI App",
        app_version="1.0.0",
        app_description="Учебное приложение на FastAPI",
        app_authors=["Иванов И.И.", "Петров П.П."],
    )

    runtime_service = RuntimeConfigService(
        initial_config=RuntimeConfigModel(
            log_level="INFO",
            feature_flag=False,
            maintenance_mode=False,
            runtime_message="Приложение работает в штатном режиме",
        )
    )

    return {"app_config": static_config, "runtime_config_service": runtime_service}
