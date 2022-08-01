from datetime import datetime

from sqlalchemy import (Column, SmallInteger,
                        ForeignKey, VARCHAR,
                        TIMESTAMP, DECIMAL)
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Category(Base):
    __tablename__: str = "categories"

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(20), nullable=False)
    parent_id = Column(SmallInteger, ForeignKey("categories.id", ondelete="CASCADE"))


class Product(Base):
    __tablename__: str = "products"

    id = Column(SmallInteger, primary_key=True)
    category_id = Column(SmallInteger, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    name = Column(VARCHAR(24), nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.now())
    price = Column(DECIMAL(8, 2), default=0)
    description = Column(VARCHAR(140))

class Order_Item(Base):
    __tablename__: str = "order_items"

    id = Column(SmallInteger, primary_key=True, nullable=False)
    order_id = Column(SmallInteger, nullable=False)
    product_id = Column(SmallInteger, ForeignKey("products.id"), nullable=False)
    total = Column(SmallInteger, nullable=False)

class Order(Base):
    __tablename__: str = "orders"

    id = Column(SmallInteger, primary_key=True, nullable=False)

