from app.db.mongodb import order_collection, product_collection
from app.models.order import OrderCreate
from bson import ObjectId
from app.utils.pagination import paginate

async def create_order(order: OrderCreate) -> str:
    order_dict = order.dict()
    total_price = 0.0
    product_details = []

    for item in order.items:
        product = await product_collection.find_one({"_id": ObjectId(item.productId)})

        if not product:
            raise ValueError(f"Product ID {item.productId} not found")

        total_price += product["price"] * item.qty
        product_details.append({
            "productDetails": {
                "name": product["name"],
                "id": str(product["_id"])
            },
            "qty": item.qty
        })

    result = await order_collection.insert_one({
        "userId": order.userId,
        "items": product_details,
        "total": round(total_price, 2)
    })

    return str(result.inserted_id)

async def list_orders(user_id: str, limit: int = 10, offset: int = 0):
    orders_cursor = (
        order_collection
        .find({"userId": user_id})
        .skip(offset)
        .limit(limit)
        .sort("_id")
    )

    orders = []
    async for order in orders_cursor:
        orders.append({
            "id": str(order["_id"]),
            "items": order["items"],
            "total": order["total"]
        })

    return paginate(orders, offset, limit)