from pydantic import BaseModel

from .game_map import GameMapData
from .map_category import MapCategoryData


class MapData(BaseModel):
    map: GameMapData
    categories: list[MapCategoryData]

    class Config:
        frozen = True
