from fastapi import APIRouter, Query, HTTPException
from app.domain.order import service
from app.domain.order.models import Order
from typing import Optional


router = APIRouter()

@router.get("/")
async def get_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
):
    return service.list_orders(skip, limit)

@router.post("/")
async def create_item(item: Order):
    item_id = service.create_new_order(item)
    return {"message": "Item created", "id": item_id}

@router.put("/{order_id}")
async def update_item(order_id:str, item: Order):
    item_id = service.update_order(order_id, item)
    if not item_id:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item updated", "id": item_id}

@router.delete("/{order_id}")
async def delete_item(order_id: str):
    item_id = service.delete_order(order_id)
    if not item_id:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted", "id": item_id}

@router.get("/dashboard")
async def dashboard(
    category: Optional[str] = Query(None, alias="category", description="Filter by product category"),
    product: Optional[str] = Query(None, alias="product", description="Filter by product name"),
    start_date: Optional[str] = Query(None, alias="start_date", description="Start date for filtering orders (ISO format)"),
    end_date: Optional[str] = Query(None, alias="end_date", description="End date for filtering orders (ISO format)")
):
    try:
        data = service.dashboard(category=category, product=product, start_date=start_date, end_date=end_date)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))