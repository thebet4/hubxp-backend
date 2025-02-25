def individual_product(product):
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "description": product["description"],
        "price": product["price"],
        "category_id": product["category_id"],
        "image_url": product["image_url"],
        "created_at": product["created_at"],
        "updated_at": product["updated_at"]
    }


def all_products(products):
    return [individual_product(product) for product in products]
