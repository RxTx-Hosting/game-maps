from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from .map_marker import MapMarkerData


class MapCategoryData(BaseModel):
    slug: str
    name: str
    color: str
    is_visible_by_default: bool = True
    use_pin_style: bool = True
    icon: str | None = None
    default_name: str | None = None
    default_description: str | None = None
    markers: list["MapMarkerData"] = []

    class Config:
        frozen = True
