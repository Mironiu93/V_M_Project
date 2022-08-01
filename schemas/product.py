from datetime import datetime

from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    category_id: int = Field(ge=1)
    name: str = Field(max_length=24)
    date_created: datetime = Field(default=datetime.now())
    description: str = Field(max_length=140, default=None)
    price: float


class ProductInDBSchema(ProductSchema):
    id: int = Field(ge=1)
