from pydantic import BaseModel


class MapCategoryData(BaseModel):
    slug: str
    name: str
    color: str
    is_visible_by_default: bool = True
    icon: str | None = None
    default_description: str | None = None

    class Config:
        frozen = True
