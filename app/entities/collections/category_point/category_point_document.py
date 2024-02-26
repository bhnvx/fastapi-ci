import dataclasses

from app.entities.category.category_codes import CategoryCode
from app.entities.collections.base_document import BaseDocument
from app.entities.collections.geo_json import GeoJsonPoint


@dataclasses.dataclass
class CategoryPointDocument(BaseDocument):
    cache_key: str
    codes: tuple[CategoryCode, ...]
    point: GeoJsonPoint
