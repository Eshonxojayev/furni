from fastapi import FastAPI, security, HTTPException
from database import session, ENGINE
# from order_router import order_router
from product_router import product_router

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from database import session, ENGINE
from models import Product

app = FastAPI()
# app.include_router(order_router)
session = session(bind=ENGINE)


@product_router.get("/product")
async def get_products():
    products = session.query(Product).all()
    context = [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "count": product.count,
        }
        for product in products

    ]
    return jsonable_encoder(context)



@app.get("/api")
async def landing():
    return {
        "message": "This is landing page"
    }