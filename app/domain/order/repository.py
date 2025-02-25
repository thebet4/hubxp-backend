from app.core.database import db
from app.domain.order.schemas import all_orders
from app.domain.order.models import Order
from bson.objectid import ObjectId
from app.domain.product.schemas import all_products
from fastapi import  HTTPException
from typing import Dict, Optional
from datetime import datetime


collection = db["order"]
product_collection = db["product"]

def get(skip: int = 0, limit = 0):
    data = collection.find({ }).skip(skip).limit(limit)
    orders = all_orders(data)
    total_items = collection.count_documents({})

    return {
        "total": total_items,
        "count": len(orders),
        "page_size": limit,
        "items": orders
    }

def create(new_order: Order):
    # Ensure product_ids is a list, even if it has one element
    product_ids = [ObjectId(pid) for pid in new_order.get('product_ids', [])]

    # Query product details using product_ids
    product_details = product_collection.find({"_id": {"$in": product_ids}})

    products = all_products(product_details)

    total = 0
    for product in products:
        # Assuming the product has a field 'price'
        total += product['price']
    
    # Add total to the new order
    new_order['total'] = total

    # Insert the new order with the total price
    response = collection.insert_one(dict(new_order))
    
    return str(response.inserted_id)

def update(order_id: str, data: Order):
    try:
        # Convert product_ids from strings to ObjectIds
        product_ids = [ObjectId(pid) for pid in data.get('product_ids', [])]
        
        if not product_ids:
            return HTTPException(status_code=500, detail="No valid product IDs found")

        
        # Query product details using the ObjectIds
        product_details = product_collection.find({"_id": {"$in": product_ids}})
        
        total = 0
        for product in product_details:
            # Assuming the product has a field 'price'
            total += product['price']

        # Add the total to the updated order data
        data['total'] = total

        # Update the existing order by its _id
        response = collection.update_one(
            {"_id": ObjectId(order_id)},  # Find the order by its ObjectId
            {"$set": data}      # Update the order fields with new data
        )

        # Check if the update was successful
        if response.matched_count == 0:
            return
        
        return order_id
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")

def delete(order_id: str):
    try:
        id = ObjectId(order_id)
        existing_order = collection.find_one({"_id": id})

        if not existing_order:
            return
        
        collection.delete_one({"_id":id})

        return order_id
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")

def get_dashboard_data(
    category: Optional[str] = None, 
    product: Optional[str] = None, 
    start_date: Optional[str] = None, 
    end_date: Optional[str] = None
):
    match_stage = {}

    if start_date or end_date:
        match_stage["date"] = {}
        if start_date:
            match_stage["date"]["$gte"] = datetime.fromisoformat(start_date)
        if end_date:
            match_stage["date"]["$lte"] = datetime.fromisoformat(end_date)

    query = {
        "product_details.category_id": {"$in": [category]}
    }


    pipeline = [
        {"$match": match_stage} if match_stage else None,
        {"$set": {"order_id": "$_id"}},
        {"$unwind": "$product_ids"},
        {
            "$set": {
                "product_ids": { "$toObjectId": "$product_ids" }
            }
        },
        {
            "$lookup": {
                "from": "product",
                "localField": "product_ids",
                "foreignField": "_id",
                "as": "product_details"
            }
        },
        {"$unwind": "$product_details"},
        {"$match": query} if query else None,
        {"$match": {"product_details._id": ObjectId(product)}} if product else None,
        {
            "$group": {
                "_id": "$order_id",  # Agrupa pelo pedido original
                "total_value": {"$first": "$total"}  # Usa o total original do pedido
            }
        },
        {
            "$group": {
                "_id": None,
                "total_orders": {"$sum": 1},  # Contagem correta dos pedidos
                "total_revenue": {"$sum": "$total_value"},  # Soma dos totais dos pedidos
                "average_order_value": {"$avg": "$total_value"}  # Média dos pedidos
            }
        }
    ]
    # Remover etapas None do pipeline
    pipeline = [stage for stage in pipeline if stage is not None]

    # Executar a agregação
    return list(collection.aggregate(pipeline))