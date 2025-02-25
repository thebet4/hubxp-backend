from app.domain.order import repository
from app.domain.order.models import Order
from typing import Optional

def list_orders(skip: int, limit: int):
    return repository.get(skip, limit)

def create_new_order(item: Order):
    return repository.create(dict(item))

def update_order(order_id: str, item: Order):
    return repository.update(order_id, dict(item))

def delete_order(order_id: str,):
    return repository.delete(order_id)

def dashboard(
    category: Optional[str] = None, 
    product: Optional[str] = None, 
    start_date: Optional[str] = None, 
    end_date: Optional[str] = None
):
    return repository.get_dashboard_data(category=category, product=product, start_date=start_date, end_date=end_date)
