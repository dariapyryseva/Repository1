import geopandas as gpd
from shapely.geometry import Point
from src.infra_access import count_within_radius

# тестовые данные
houses = gpd.GeoDataFrame(geometry=[Point(0, 0), Point(1, 1)], crs="EPSG:4326")

objects = gpd.GeoDataFrame(geometry=[Point(0, 0)], crs="EPSG:4326")

result = count_within_radius(houses, objects, 500)

print(result)
