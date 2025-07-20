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
        "documentation_url": "/docs",
        "redoc_url": "/redoc",
        "products_url": "/products",
        "orders_url": "/orders"
        }
