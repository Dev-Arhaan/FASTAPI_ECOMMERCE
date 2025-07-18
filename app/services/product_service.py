from app.db.mongodb import product_collection
from app.models.product import ProductCreate, ProductListItem
from typing import Optional
from app.utils.pagination import paginate

import re


async def create_product(product: ProductCreate) -> str:
    product_dict = product.dict()
    result = await product_collection.insert_one(product_dict)
    return str(result.inserted_id)

async def list_products(name: Optional[str], size: Optional[str], limit: int, offset: int):
    query = {}

    if name:
        query["name"] = { "$regex": re.escape(name), "$options": "i" }

    if size:
        query["sizes.size"] = size  # array field filter

    cursor = (
        product_collection
        .find(query)
        .skip(offset)
        .limit(limit)
        .sort("_id")
    )

    products = []
    async for product in cursor:
        products.append({
            "id": str(product["_id"]),
            "name": product["name"],
            "price": product["price"]
        })

    return paginate(products, offset, limit)

