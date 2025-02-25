from app.core.database import db
from app.domain.category.schemas import all_categories
from app.domain.product.schemas import all_products
from app.domain.category.models import Category
from bson.objectid import ObjectId

collection = db["category"]
product_collection = db["product"]

def get(skip: int = 0, limit = 0, name: str =""):
    query = {}

    # Add name filter if provided
    if name:
        query["name"] = {"$regex": name, "$options": "i"}  # Case-insensitive search
    
    data = collection.find(query).skip(skip).limit(limit)

    categories = all_categories(data)
    total_items = collection.count_documents({})

    return {
        "total": total_items,
        "count": len(categories),
        "page_size": limit,
        "items": categories
    }

def create(new_category: Category):
    response = collection.insert_one(dict(new_category))
    return str(response.inserted_id)
    
def update(category_id: str, data: Category):
    try:
        id = ObjectId(category_id)
        
        exit_category = collection.find_one({"_id": id})

        if not exit_category:
            return

        collection.update_one({"_id":id}, {"$set":dict(data)})

        return category_id

    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")

def delete(category_id: str):
    try:
        id = ObjectId(category_id)
        exit_category = collection.find_one({"_id": id})

        if not exit_category:
            return
        
        # Remove deleted category from all products
        product_collection.update_many(
            {},  # Apply to all documents
            {"$pull": {"category_ids": category_id}}
        )
        
        collection.delete_one({"_id":id})

        return category_id
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")


