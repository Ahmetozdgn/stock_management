from sqlalchemy.orm import Session
from app import models, schemas
from app.auth import get_password_hash

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(name=product.name, price=product.price, stock=0)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

def adjust_stock(db: Session, product_id: int, amount: int):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        return {"error": "Product not found"}
    product.stock += amount
    db.commit()
    db.refresh(product)
    return {"message": f"Stock adjusted by {amount}", "new_stock": product.stock}
