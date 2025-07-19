from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_DB")

client = AsyncIOMotorClient(MONGO_URI)
database = client["ecommerce"]

product_collection = database.get_collection("products")
order_collection = database.get_collection("orders")
