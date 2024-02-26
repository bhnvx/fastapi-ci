import dataclasses
from typing import Sequence

from app.entities.category.categories import Category


@dataclasses.dataclass
class CategoryResponse:
    categories: Sequence[Category]
