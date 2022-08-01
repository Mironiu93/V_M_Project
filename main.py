from crud import CRUDCategory


CRUDCategory.delete(category_id=2)
category = CRUDCategory.get(category_id=2)
print(category)
