class Categories(BaseModel):
    id: int
    parent_id: int
    is_published: bool
    name_en: str
    name: str