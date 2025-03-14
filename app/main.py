from fastapi import FastAPI, APIRouter
from app.domain.product.routes import router as product_router
from app.domain.category.routes import router as category_router
from app.domain.order.routes import router as order_router


app = FastAPI()
router = APIRouter()

# Register Routes
app.include_router(product_router, prefix="/product", tags=["Products"])
app.include_router(category_router, prefix="/category", tags=["Categories"])
app.include_router(order_router, prefix="/order", tags=["Orders"])


@router.get("/")
def hello():
    return {"hello": "welcome to fastapi!"}


app.include_router(router)
