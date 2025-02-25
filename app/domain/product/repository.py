from app.core.database import db
from app.domain.product.schemas import all_products
from app.domain.product.models import Product
from bson.objectid import ObjectId
from fastapi import  HTTPException
from datetime import datetime

collection = db["items"]


def get(skip: int = 0, limit: int = 0, name: str = ""):

    query = {}

    # Add name filter if provided
    if name:
        query["name"] = {"$regex": name, "$options": "i"}  # Case-insensitive search

    data = collection.find(query).skip(skip).limit(limit)
    

    # Convert MongoDB ObjectId to string
    items = all_products(data)
    total_items = collection.count_documents({})

    return {
        "total": total_items,
        "count": len(items),
        "page_size": limit,
        "items": items
    }

def create(new_product: Product):
    response = collection.insert_one(dict(new_product))
    return str(response.inserted_id)
    
def update(product_id: str, data: Product):
    try:
        id = ObjectId(product_id)
        
        exit_product = collection.find_one({"_id": id})

        if not exit_product:
            return

        collection.update_one({"_id":id}, {"$set":dict(data)})

        return product_id

    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")

def delete(product_id: str):
    try:
        id = ObjectId(product_id)
        exit_product = collection.find_one({"_id": id})

        if not exit_product:
            return
        
        collection.delete_one({"_id":id})

        return product_id

    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")
