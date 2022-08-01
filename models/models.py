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
    is_published = Column(Boolean, default=False)
    parent_id = Column(SmallInteger, ForeignKey("products.id", ondelete="CASCADE"))


class Product(Base):
    __tablename__: str = "products"

    id = Column(SmallInteger, primary_key=True, ForeignKey("order_items.product_id"))
    category_id = Column(SmallInteger, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    name = Column(VARCHAR(24), nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.now())
    price = Column(DECIMAL(8, 2), default=0)
    description = Column(VARCHAR(140))
    is_published = Column(Boolean, default=False)

class Order_Item(Base):
    __tablename__: str = "order_items"

    id = Column(SmallInteger, primary_key=True, nullable=False)
    order_id = Column(SmallInteger, nullable=False, ForeignKey("orders.id"))
    product_id = Column(SmallInteger, ForeignKey("products.id"), nullable=False)
    total = Column(SmallInteger, nullable=False)

class Order(Base):
    __tablename__: str = "orders"

    id = Column(SmallInteger, primary_key=True, nullable=False, ForeignKey("order_items.order_id"))
    bot_user_id = Column(SmallInteger, ForeignKey("bot_users.id"))
    date_create = Column(TIMESTAMP, default=datetime.now())
    status_id = Column(SmallInteger, ForeignKey("statuses.id"))
    invoice_id = Column(VARCHAR(24), nullable=False, ForeignKey("invoices.id"))

class Status(Base):
    __tablename__: str = "statuses"

    id = Column(SmallInteger, primary_key=True, nullable=False, ForeignKey("orders.status_id"), ForeignKey("invoices.status_id"))
    name = Column(VARCHAR(24), nullable=False)

class Bot_User(Base):
    __tablename__: str = "bot_users"

    id = Column(VARCHAR(24), primary_key=True, nullable=False, ForeignKey("orders.bot_user_id"), ForeignKey("inovoices.bot_user_id"))
    is_blocked = Column(Boolean, default=False)
    balance = Column(SmallInteger, nullable=False)
    language_id = Column(SmallInteger, ForeignKey("languages.id"))

class Invoice(Base):
    __tablename__ : str = "invoices"

    id = Column(VARCHAR(24), primary_key=True, nullable=False, ForeignKey("orders.invoice_id"))
    bot_user_id = Column(SmallInteger, ForeignKey("bot_users.id"))
    dete_created = Column(TIMESTAMP, default=datetime.now())
    total = Column(SmallInteger, nullable=False)
    status_id = Column(SmallInteger, nullable=False, ForeignKey("statuses.id"))

class Language(Base):
    __tablename__ : str = "languages"

    id = Column(SmallInteger, primary_key=True, nullable=False, ForeignKey("bot_users.language_id"))
    language_code = Column(VARCHAR(3))
