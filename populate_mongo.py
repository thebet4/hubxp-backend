import typer
import random
from faker import Faker
from datetime import datetime
from app.core.database import db

# Initialize Typer and Faker
app = typer.Typer()
fake = Faker()

# Database collections
products_collection = db["product"]
categories_collection = db["category"]
orders_collection = db["order"]

# Sample categories
CATEGORIES = ["Electronics", "Clothing", "Food", "Books", "Toys"]
NOW = int(datetime.timestamp(datetime.now()))


def generate_categories():
    """Populate the categories collection."""
    categories = [
        {
            "name": category, 
            "created_at": NOW, 
            "updated_at": NOW
        } for category in CATEGORIES
    ]

    categories_collection.insert_many(categories)

    return categories

def generate_products(n=50):
    """Populate the products collection."""
    categories = list(categories_collection.find())
    products = []
    for _ in range(n):
        category = random.choice(categories)
        product = {
            "name": fake.word().capitalize(),
            "description": fake.word().capitalize(),
            "price": round(random.uniform(100, 10000), 0),
            "category_id": [str(category["_id"])],
            "image_url": "http://localhost:8000",
            "created_at": NOW, 
            "updated_at": NOW
        }
        products.append(product)
    products_collection.insert_many(products)
    return products

def generate_orders(n=20):
    """Populate the orders collection."""
    products = list(products_collection.find())
    orders = []
    for _ in range(n):
        num_items = random.randint(1, 5)
        items = random.sample(products, num_items)
        total = sum(item["price"] for item in items)
        random_datetime = fake.date_time_between(start_date="-6M", end_date="now")
        order = {
            "product_ids": [str(item["_id"]) for item in items],
            "total": round(total, 2),
            "date": random_datetime,
            "created_at": NOW, 
            "updated_at": NOW
        }
        orders.append(order)
    orders_collection.insert_many(orders)
    return orders

def populate():
    """Populate the MongoDB database with fake data."""
    db["category"].drop()
    db.drop_collection("product")
    db.drop_collection("order")
    
    generate_categories()
    generate_products()
    generate_orders()
    typer.echo("Database successfully populated! ✅")

populate()
