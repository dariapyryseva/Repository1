import geopandas as gpd
from loguru import logger

from ..core.spatial import create_buffer
from ..exceptions import EmptyDataError
from ..utils.geo import ensure_same_crs, to_metric_crs


def count_within_radius(houses_gdf, objects_gdf, radius):
    if houses_gdf.empty or objects_gdf.empty:
        raise EmptyDataError("Пустые данные")

    ensure_same_crs(houses_gdf, objects_gdf)

    houses = to_metric_crs(houses_gdf)
    objects = to_metric_crs(objects_gdf)

    buffers = create_buffer(objects, radius)

    buffers_gdf = gpd.GeoDataFrame(geometry=buffers, crs=houses.crs)

    joined = gpd.sjoin(houses, buffers_gdf, predicate="intersects")

    return joined.groupby(joined.index).size()


def unserved_objects(houses_gdf, objects_gdf, radius):
    counts = count_within_radius(houses_gdf, objects_gdf, radius)
    return houses_gdf.loc[~houses_gdf.index.isin(counts.index)]


def accessibility_ratio(houses_gdf, objects_gdf, radius):
    counts = count_within_radius(houses_gdf, objects_gdf, radius)
    return len(counts) / len(houses_gdf)
