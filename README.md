# REST API - FastAPI + MongoDB

This repository contains the backend implementation of a Full Stack application using FastAPI and MongoDB. It provides a RESTful API with CRUD operations for Products, Categories, and Orders, along with a dashboard for sales metrics.

## 🚀 Technologies Used

- **FastAPI** - High-performance web framework for APIs
- **MongoDB** - NoSQL database for data storage
- **Pydantic** - Data validation and serialization
- **Uvicorn** - ASGI server for running FastAPI
- **Docker** - Containerization for environment consistency
- **Serverless Framework** - For deploying Lambda functions
- **LocalStack** - AWS services emulation (S3)

---

## 📌 Features

- **CRUD Operations**: Products, Categories, Orders
- **Many-to-Many Relationships**: Products ↔ Categories
- **Sales Dashboard**: Aggregated data on orders, revenue, and KPIs
- **Task Automation**: AWS Lambda function for background processing

---

## 🛠️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/thebet4/rest-fast-api
cd your-repository
```

### 2️⃣ Set Up a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Start the Application

```bash
uvicorn app.main:app --reload
```

FastAPI will be available at:  
📍 `http://127.0.0.1:8000`

---

## 📊 API Documentation

FastAPI provides automatic documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔗 Endpoints

### 📦 Products
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/products` | List all products |
| POST | `/products` | Create a new product |
| GET | `/products/{id}` | Get a specific product |
| PUT | `/products/{id}` | Update a product |
| DELETE | `/products/{id}` | Delete a product |

### 🍿 Categories
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/categories` | List all categories |
| POST | `/categories` | Create a new category |
| GET | `/categories/{id}` | Get a specific category |
| PUT | `/categories/{id}` | Update a category |
| DELETE | `/categories/{id}` | Delete a category |

### 🛒 Orders
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/orders` | List all orders |
| GET | `/orders/dashboard` | Get orders metrics |
| POST | `/orders` | Create a new order |
| GET | `/orders/{id}` | Get a specific order |
| PUT | `/orders/{id}` | Update an order |
| DELETE | `/orders/{id}` | Delete an order |

---

## 💃🏻👮🏻 Database Schema

- **Product**: `id`, `name`, `description`, `price`, `category_ids`, `image_url`
- **Category**: `id`, `name`
- **Order**: `id`, `date`, `product_ids`, `total`

---

## 🏰 Running with Docker

To spin up the environment using Docker, run:

```bash
./run
```

---

## 📆 Populating the Database

Run the script to generate test data:

```bash
python populate_mongo.py
```

---

## 🚀 Serverless Task (Lambda)

The backend includes a Serverless function for background tasks like:

- Processing sales reports
- Sending order notifications

Deploy with:

```bash
serverless deploy
```

---

## 📝 License

This project is licensed under the MIT License.

---

🚀 **Happy Coding!**

