def individual_order(order):
    return {
        "id": str(order["_id"]),
        "date": order["date"],
        "product_ids": order["product_ids"],
        "total": order["total"],
        "created_at": order["created_at"],
        "updated_at": order["updated_at"]
    }


def all_orders(orders):
    return [individual_order(order) for order in orders]
