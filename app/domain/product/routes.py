from fastapi import APIRouter, Query, HTTPException
from app.domain.product import service
from app.domain.product.models import Product

router = APIRouter()

@router.get("/")
async def get_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    name: str = None
):
    return service.list_products(skip, limit, name)

@router.post("/")
async def create_item(item: Product):
    item_id = service.create_new_product(item)
    return {"message": "Item created", "id": item_id}

@router.put("/{product_id}")
async def update_item(product_id:str, item: Product):
    item_id = service.update_product(product_id, item)
    if not item_id:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item updated", "id": item_id}

@router.delete("/{product_id}")
async def delete_item(product_id: str):
    item_id = service.delete_product(product_id)
    if not item_id:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted", "id": item_id}
