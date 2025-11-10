import random
from sqlalchemy.orm import Session
from app.models import Product

def predict_future_stock(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return {"error": "Product not found"}
    # Basit tahmin simülasyonu
    simulated_future = product.stock + random.randint(-5, 10)
    return {"product": product.name, "current_stock": product.stock, "predicted_next_week": simulated_future}
