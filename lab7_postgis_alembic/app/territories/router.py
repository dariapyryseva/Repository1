from app.common.db import get_db
from app.territories import crud, schemas
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/territories", tags=["territories"])


# ========== Territory Endpoints ==========
@router.post(
    "/", response_model=schemas.TerritoryRead, status_code=status.HTTP_201_CREATED
)
def create_territory(data: schemas.TerritoryCreate, db: Session = Depends(get_db)):
    """Создать новую территорию"""
    return crud.create_territory(db, data)


@router.get("/", response_model=list[schemas.TerritoryRead])
def list_territories(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    """Получить список территорий"""
    return crud.list_territories(db, limit=limit, offset=offset)


@router.get("/intersects", response_model=list[schemas.TerritoryRead])
def list_intersecting_territories(
    wkt: str = Query(..., description="WKT геометрия для поиска пересечений"),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    """Найти территории, пересекающиеся с заданной WKT-геометрией"""
    return crud.list_intersecting_territories(db, wkt, limit=limit, offset=offset)


@router.get("/{territory_id}", response_model=schemas.TerritoryRead)
def get_territory(territory_id: int, db: Session = Depends(get_db)):
    """Получить территорию по ID"""
    territory = crud.get_territory(db, territory_id)
    if not territory:
        raise HTTPException(status_code=404, detail="Territory not found")
    return territory


@router.put("/{territory_id}", response_model=schemas.TerritoryRead)
def update_territory(
    territory_id: int, data: schemas.TerritoryUpdate, db: Session = Depends(get_db)
):
    """Обновить территорию"""
    territory = crud.update_territory(db, territory_id, data)
    if not territory:
        raise HTTPException(status_code=404, detail="Territory not found")
    return territory


@router.delete("/{territory_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_territory(territory_id: int, db: Session = Depends(get_db)):
    """Удалить территорию"""
    if not crud.delete_territory(db, territory_id):
        raise HTTPException(status_code=404, detail="Territory not found")
    return None


# ========== TerritoryMetric Endpoints ==========
@router.post(
    "/{territory_id}/metrics",
    response_model=schemas.TerritoryMetricRead,
    status_code=status.HTTP_201_CREATED,
)
def create_metric(
    territory_id: int,
    data: schemas.TerritoryMetricCreate,
    db: Session = Depends(get_db),
):
    """Создать показатель для территории"""
    territory = crud.get_territory(db, territory_id)
    if not territory:
        raise HTTPException(status_code=404, detail="Territory not found")
    return crud.create_metric(db, territory_id, data)


@router.get("/{territory_id}/metrics", response_model=list[schemas.TerritoryMetricRead])
def list_metrics(territory_id: int, db: Session = Depends(get_db)):
    """Получить все показатели территории"""
    territory = crud.get_territory(db, territory_id)
    if not territory:
        raise HTTPException(status_code=404, detail="Territory not found")
    return crud.list_metrics_by_territory(db, territory_id)


@router.put(
    "/{territory_id}/metrics/{metric_id}", response_model=schemas.TerritoryMetricRead
)
def update_metric(
    territory_id: int,
    metric_id: int,
    data: schemas.TerritoryMetricUpdate,
    db: Session = Depends(get_db),
):
    """Обновить показатель территории"""
    territory = crud.get_territory(db, territory_id)
    if not territory:
        raise HTTPException(status_code=404, detail="Territory not found")

    metric = crud.update_metric(db, metric_id, data)
    if not metric or metric.territory_id != territory_id:
        raise HTTPException(status_code=404, detail="Metric not found")
    return metric


@router.delete(
    "/{territory_id}/metrics/{metric_id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete_metric(territory_id: int, metric_id: int, db: Session = Depends(get_db)):
    """Удалить показатель территории"""
    territory = crud.get_territory(db, territory_id)
    if not territory:
        raise HTTPException(status_code=404, detail="Territory not found")

    if not crud.delete_metric(db, metric_id):
        raise HTTPException(status_code=404, detail="Metric not found")
    return None
