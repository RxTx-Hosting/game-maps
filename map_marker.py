from pydantic import BaseModel


class MapMarkerData(BaseModel):
    name: str
    category_slug: str
    position_x: float
    position_y: float
    description: str | None = None
    icon: str | None = None

    class Config:
        frozen = True
