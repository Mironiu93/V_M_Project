from pydantic import BaseModel, Field


class CategorySchema(BaseModel):
    name: str = Field(max_length=20)
    parent_id: int = Field(default=None, ge=1)


class CategoryInDBSchema(CategorySchema):
    id: int = Field(ge=1)
