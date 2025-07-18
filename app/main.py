from fastapi import FastAPI
from app.routers import products 
from app.routers import products, orders


app = FastAPI()

app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

@app.get("/")
async def root():
    return {"message": "Ecommerce backend running"}
