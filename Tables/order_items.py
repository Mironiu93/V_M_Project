class OrderItems(Products, Orders):
    id: int
    order_id: int
    product_id: int
    total: int