from fastapi import APIRouter, Query, HTTPException
from app.domain.category import service
from app.domain.category.models import Category

router = APIRouter()

@router.get("/")
async def get_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    name: str = None
):
    return service.list_categories(skip, limit, name)

@router.post("/")
async def create_item(item: Category):
    item_id = service.create_new_category(item)
    return {"message": "Item created", "id": item_id}

@router.put("/{category_id}")
async def update_item(category_id:str, item: Category):
    item_id = service.update_category(category_id, item)
    if not item_id:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item updated", "id": item_id}

@router.delete("/{category_id}")
async def delete_item(category_id: str):
    item_id = service.delete_category(category_id)
    if not item_id:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted", "id": item_id}
 