from pydantic import BaseModel


class GridStyleOptions(BaseModel):
    line_color: str = "#ffffff"
    line_opacity: float = 0.5
    line_weight: float = 1.5
    label_color: str = "#ffffff"
    label_opacity: float = 0.7
    label_size: int = 20

    class Config:
        frozen = True


class GameMapData(BaseModel):
    name: str
    slug: str
    description: str | None = None
    image_url: str
    image_width: int
    image_height: int
    min_zoom: int
    max_zoom: int
    default_zoom: int
    default_center_x: float
    default_center_y: float
    grid_system: str | None = None
    grid_options: GridStyleOptions | None = None

    class Config:
        frozen = True
