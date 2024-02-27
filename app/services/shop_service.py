from app.dtos.shop.shop_creation_request import ShopCreationRequest
from app.entities.caches.category_point.category_point_cache_invalidator import (
    ShopCreationCategoryPointCacheInvalidator,
)
from app.entities.collections import ShopCollection
from app.entities.collections.shop.shop_document import (
    ShopDeliveryAreaSubDocument,
    ShopDocument,
)


async def create_shop(shop_creation_request: ShopCreationRequest) -> ShopDocument:
    shop = await ShopCollection.insert_one(
        shop_creation_request.name,
        list(shop_creation_request.category_codes),
        [ShopDeliveryAreaSubDocument(poly=area) for area in shop_creation_request.delivery_areas],
    )

    await ShopCreationCategoryPointCacheInvalidator(shop).invalidate()

    return shop
