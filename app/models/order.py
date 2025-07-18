from pydantic import BaseModel, Field
from typing import List


class OrderItem(BaseModel):
    productId: str
    qty: int = Field(..., gt=0)


class OrderCreate(BaseModel):
    userId: str
    items: List[OrderItem]


class OrderResponse(BaseModel):
    id: str


class ProductDetails(BaseModel):
    name: str
    id: str


class OrderItemResponse(BaseModel):
    productDetails: ProductDetails
    qty: int


class OrderDataResponse(BaseModel):
    id: str
    items: List[OrderItemResponse]
    total: float


class PaginatedOrderResponse(BaseModel):
    data: List[OrderDataResponse]
    page: dict  # Optional: you can replace this with a structured PageInfo model later
