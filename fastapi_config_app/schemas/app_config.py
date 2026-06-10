from typing import List

from pydantic import BaseModel


class AppConfigModel(BaseModel):
    app_name: str
    app_version: str
    app_description: str
    app_authors: List[str]
