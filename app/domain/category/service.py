from app.domain.category import repository
from app.domain.category.models import Category

def list_categories(skip: int, limit: int, name: str = None):
    return repository.get(skip, limit, name)

def create_new_category(item: Category):
    return repository.create(dict(item))

def update_category(category_id: str, updated_category: Category):
    return repository.update(category_id, dict(updated_category))

def delete_category(category_id: str,):
    return repository.delete(category_id)
