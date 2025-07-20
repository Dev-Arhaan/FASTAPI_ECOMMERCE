from fastapi import FastAPI
from app.routers import products, orders


app = FastAPI()

app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

@app.get("/")
async def root():
    return {
        "message": "Ecommerce backend running",
        "version": "1.0.0",
        "documentation_url": "http://localhost:8000/docs",
        "redoc_url": "http://localhost:8000/redoc",
        "products_url": "http://localhost:8000/products",
        "orders_url": "http://localhost:8000/orders"
        }
