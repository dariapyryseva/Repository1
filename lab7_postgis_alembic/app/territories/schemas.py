from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


# ========== Territory Schemas ==========
class TerritoryBase(BaseModel):
    name: str = Field(..., max_length=255)
    territory_type: str = Field(..., max_length=100)
    level: int = Field(..., ge=0)
    description: Optional[str] = Field(None, max_length=500)
    geom_wkt: str  # WKT representation of geometry


class TerritoryCreate(TerritoryBase):
    pass


class TerritoryUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    territory_type: Optional[str] = Field(None, max_length=100)
    level: Optional[int] = Field(None, ge=0)
    description: Optional[str] = Field(None, max_length=500)
    geom_wkt: Optional[str] = None


class TerritoryRead(BaseModel):
    id: int
    name: str
    territory_type: str
    level: int
    description: Optional[str] = None
    geom_wkt: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ========== TerritoryMetric Schemas ==========
class TerritoryMetricBase(BaseModel):
    year: int = Field(..., ge=1900, le=2100)
    population: Optional[int] = Field(None, ge=0)
    area_km2: Optional[Decimal] = Field(None, ge=0)
    source: Optional[str] = Field(None, max_length=255)


class TerritoryMetricCreate(TerritoryMetricBase):
    pass


class TerritoryMetricUpdate(BaseModel):
    year: Optional[int] = Field(None, ge=1900, le=2100)
    population: Optional[int] = Field(None, ge=0)
    area_km2: Optional[Decimal] = Field(None, ge=0)
    source: Optional[str] = Field(None, max_length=255)


class TerritoryMetricRead(BaseModel):
    id: int
    territory_id: int
    year: int
    population: Optional[int] = None
    area_km2: Optional[Decimal] = None
    source: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
