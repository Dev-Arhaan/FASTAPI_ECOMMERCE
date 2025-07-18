from fastapi import APIRouter, status, HTTPException, Query
from app.models.order import OrderCreate, OrderResponse, PaginatedOrderResponse
from app.services.order_service import create_order, list_orders

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OrderResponse)
async def create_order_api(order: OrderCreate):
    try:
        order_id = await create_order(order)
        return {"id": order_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=PaginatedOrderResponse)
async def get_orders_api(
    user_id: str,
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0)
):
    return await list_orders(user_id, limit, offset)
