from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Request
import os

MONGO_URI = "mongodb://localhost:27017" 

client = AsyncIOMotorClient(MONGO_URI)
database = client["ecommerce"]

product_collection = database.get_collection("products")
order_collection = database.get_collection("orders")
