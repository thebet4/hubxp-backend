from fastapi import FastAPI, APIRouter
from app.domain.product.routes import router as product_router


app = FastAPI()
router = APIRouter()

# Register Routes
app.include_router(product_router, prefix="/product", tags=["Products"])


app.include_router(router)
