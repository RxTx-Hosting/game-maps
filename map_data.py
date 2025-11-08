from pydantic import BaseModel

from .game_map import GameMapData
from .map_category import MapCategoryData
from .map_marker import MapMarkerData


class MapData(BaseModel):
    map: GameMapData
    categories: list[MapCategoryData]
    markers: list[MapMarkerData]

    class Config:
        frozen = True
