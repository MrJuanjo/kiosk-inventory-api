from sqlalchemy.orm import Session

from app import schemas
from app.models import Product
from app.schemas import ProductCreate


def create_product(db: Session, product: ProductCreate) -> Product:
    product_data = product.model_dump()
    db_product = Product(**product_data)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()


def update_product(db: Session, product_id: int, product_data: schemas.ProductCreate):
    db_product = get_product(db, product_id)
    if not db_product:
        return None

    for key, value in product_data.model_dump().items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        return None

    db.delete(db_product)
    db.commit()
    return db_product
