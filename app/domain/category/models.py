
from pydantic import BaseModel
from datetime import datetime

class Category(BaseModel):
    name: str
    created_at: int = int(datetime.timestamp(datetime.now()))
    updated_at: int = int(datetime.timestamp(datetime.now()))
