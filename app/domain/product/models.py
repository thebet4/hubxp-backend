from pydantic import BaseModel
from datetime import datetime

class Product(BaseModel):
    name: str
    description: str
    price: int = 0
    category_ids: list[str] = []
    image_url: str
    created_at: int = int(datetime.timestamp(datetime.now()))
    updated_at: int = int(datetime.timestamp(datetime.now()))
