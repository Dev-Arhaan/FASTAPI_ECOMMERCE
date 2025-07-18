from fastapi import APIRouter, status, Query
from app.models.product import ProductCreate, ProductResponse, PaginatedProductResponse
from app.services.product_service import list_products
from typing import Optional
from app.services.product_service import create_product

router = APIRouter()

@router.post(
    "/", 
    status_code=status.HTTP_201_CREATED, 
    response_model=ProductResponse
)
async def create_product_api(product: ProductCreate):
    product_id = await create_product(product)
    return {"id": product_id}

@router.get("/", response_model=PaginatedProductResponse)
async def get_products_api(
    name: Optional[str] = None,
    size: Optional[str] = None,
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0)
):
    return await list_products(name, size, limit, offset)
