from pydantic import BaseModel, Field
from typing import List


class SizeItem(BaseModel):
    size: str
    quantity: int


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    sizes: List[SizeItem]


class ProductResponse(BaseModel):
    id: str

class ProductListItem(BaseModel):
    id: str
    name: str
    price: float


class PaginatedProductResponse(BaseModel):
    data: List[ProductListItem]
    page: dict