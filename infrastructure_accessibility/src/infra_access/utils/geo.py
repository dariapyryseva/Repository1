import geopandas as gpd

from ..exceptions import CRSMatchError


def ensure_same_crs(gdf1, gdf2):
    if gdf1.crs != gdf2.crs:
        raise CRSMatchError("CRS не совпадают")


def to_metric_crs(gdf):
    return gdf.to_crs(epsg=3857)
