from app.territories.models import Territory, TerritoryMetric
from app.territories.schemas import (
    TerritoryCreate,
    TerritoryMetricCreate,
    TerritoryMetricUpdate,
    TerritoryUpdate,
)
from geoalchemy2.elements import WKTElement
from geoalchemy2.shape import from_shape
from sqlalchemy import func, select
from sqlalchemy.orm import Session


def _territory_select():
    return select(
        Territory.id,
        Territory.name,
        Territory.territory_type,
        Territory.level,
        Territory.description,
        func.ST_AsText(Territory.geom).label("geom_wkt"),
        Territory.created_at,
    )


def get_territory(db: Session, territory_id: int):
    stmt = _territory_select().where(Territory.id == territory_id)
    return db.execute(stmt).first()


def list_territories(db: Session, limit: int = 100, offset: int = 0):
    stmt = _territory_select().order_by(Territory.id).limit(limit).offset(offset)
    return db.execute(stmt).all()


def create_territory(db: Session, data: TerritoryCreate):
    geom = WKTElement(data.geom_wkt, srid=4326)

    obj = Territory(
        name=data.name,
        territory_type=data.territory_type,
        level=data.level,
        description=data.description,
        geom=geom,
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)

    return get_territory(db, obj.id)


def update_territory(db: Session, territory_id: int, data: TerritoryUpdate):
    obj = db.get(Territory, territory_id)
    if not obj:
        return None

    update_data = data.model_dump(exclude_unset=True)

    if "geom_wkt" in update_data:
        obj.geom = WKTElement(update_data.pop("geom_wkt"), srid=4326)

    for key, value in update_data.items():
        setattr(obj, key, value)

    db.commit()
    db.refresh(obj)

    return get_territory(db, territory_id)


def delete_territory(db: Session, territory_id: int):
    obj = db.get(Territory, territory_id)
    if not obj:
        return False

    db.delete(obj)
    db.commit()
    return True


from sqlalchemy import func, select


def list_intersecting_territories(db, wkt, limit=100, offset=0):
    search_geom = func.ST_GeomFromText(wkt, 4326)

    stmt = (
        select(
            Territory.id,
            Territory.name,
            Territory.territory_type,
            Territory.level,
            Territory.description,
            func.ST_AsText(Territory.geom).label("geom_wkt"),
            Territory.created_at,
        )
        .where(func.ST_Intersects(Territory.geom, search_geom))
        .limit(limit)
        .offset(offset)
    )

    return db.execute(stmt).mappings().all()


def create_metric(db: Session, territory_id: int, data: TerritoryMetricCreate):
    obj = TerritoryMetric(
        territory_id=territory_id,
        year=data.year,
        population=data.population,
        area_km2=data.area_km2,
        source=data.source,
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)

    return obj


def list_metrics_by_territory(db: Session, territory_id: int):
    stmt = (
        select(TerritoryMetric)
        .where(TerritoryMetric.territory_id == territory_id)
        .order_by(TerritoryMetric.year)
    )

    return db.execute(stmt).scalars().all()


def update_metric(db: Session, metric_id: int, data: TerritoryMetricUpdate):
    obj = db.get(TerritoryMetric, metric_id)
    if not obj:
        return None

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(obj, key, value)

    db.commit()
    db.refresh(obj)

    return obj


def delete_metric(db: Session, metric_id: int):
    obj = db.get(TerritoryMetric, metric_id)
    if not obj:
        return False

    db.delete(obj)
    db.commit()
    return True
