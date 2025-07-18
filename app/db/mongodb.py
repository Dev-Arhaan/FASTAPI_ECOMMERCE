from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017" 

client = AsyncIOMotorClient(MONGO_URI)
database = client["ecommerce"]

product_collection = database.get_collection("products")
order_collection = database.get_collection("orders")
