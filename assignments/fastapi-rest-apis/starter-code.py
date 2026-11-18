from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Building REST APIs with FastAPI")


class ProductInput(BaseModel):
    name: str
    price: float = Field(gt=0)


class Product(ProductInput):
    id: int


products: list[Product] = [Product(id=1, name="Notebook", price=4.5)]
next_product_id = 2


# TODO: Add GET / and GET /health.
# TODO: Add GET /products and GET /products/{product_id}.
# TODO: Add POST, PUT, and DELETE routes for products.
