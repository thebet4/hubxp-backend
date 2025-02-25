from app.domain.product import repository
from app.domain.product.models import Product

def list_products(skip: int, limit: int, name: str = None):
    return repository.get(skip, limit, name)

def create_new_product(item: Product):
    return repository.create(dict(item))

def update_product(product_id: str, updated_product: Product):
    return repository.update(product_id, dict(updated_product))

def delete_product(product_id: str,):
    return repository.delete(product_id)
