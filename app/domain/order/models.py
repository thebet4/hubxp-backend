from pydantic import BaseModel
from datetime import datetime

class Order(BaseModel):
    date: datetime
    product_ids: list[str] = []
    total: int = int(0)
    created_at: int = int(datetime.timestamp(datetime.now()))
    updated_at: int = int(datetime.timestamp(datetime.now()))
