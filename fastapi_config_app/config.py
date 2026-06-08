from pydantic import BaseModel


class AppConfig(BaseModel):
    app_name: str = "Laboratory FastAPI App"
    app_version: str = "1.0.0"
    app_description: str = "Учебное приложение"
    app_authors: list[str] = ["Дарья"]


class RuntimeConfig(BaseModel):
    log_level: str = "INFO"
    feature_flag: bool = False
    maintenance_mode: bool = False
    runtime_message: str = "Application running"


# статическая конфигурация
app_config = AppConfig()

# runtime-конфигурация
runtime_config = RuntimeConfig()
