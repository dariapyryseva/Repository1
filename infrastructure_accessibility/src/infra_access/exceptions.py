class EmptyDataError(Exception):
    """Ошибка: переданы пустые GeoDataFrame"""

    pass


class CRSMatchError(Exception):
    """Ошибка: системы координат не совпадают"""

    pass
