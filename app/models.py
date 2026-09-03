from sqlalchemy import Boolean, Column, Integer, Numeric, String

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Numeric(precision=8, scale=2), nullable=False)
    category = Column(String(100), default="Not specified", nullable=True)
    stock_quantity = Column(Integer, nullable=False, default=0)
    has_discount = Column(Boolean, default=False, nullable=True)
