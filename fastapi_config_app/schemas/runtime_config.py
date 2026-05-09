from typing import Literal

from pydantic import BaseModel


class RuntimeConfigModel(BaseModel):
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"]
    feature_flag: bool
    maintenance_mode: bool
    runtime_message: str


RuntimeConfigUpdateModel = RuntimeConfigModel
