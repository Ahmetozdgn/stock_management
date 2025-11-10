from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import models, database, auth

app = FastAPI(title="Stock Management API", version="1.0")
database.init_db()

# ---------------- REGISTER ----------------
@app.post("/register", response_model=models.UserResponse)
def register(user: models.UserCreate, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = auth.get_password_hash(user.password)
    new_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# ---------------- LOGIN ----------------
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# ---------------- PRODUCTS ----------------
@app.post("/products/", response_model=models.ProductResponse)
def create_product(product: models.ProductCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    db_product = db.query(models.Product).filter(models.Product.name == product.name).first()
    if db_product:
        raise HTTPException(status_code=400, detail="Product already exists")
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.get("/products/", response_model=list[models.ProductResponse])
def read_products(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return db.query(models.Product).all()

# ---------------- STOCK ADJUST ----------------
@app.post("/stock/{product_id}/adjust")
def adjust_stock(product_id: int, amount: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product.stock += amount
    db.commit()
    db.refresh(product)
    return {"product_id": product.id, "new_stock": product.stock}

# ---------------- AI PREDICT ----------------
@app.get("/ai/predict/{product_id}")
def ai_predict(product_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    # Basit bir tahmin algoritması: stokun %10 artacağını tahmin ediyoruz
    predicted_stock = int(product.stock * 1.1)
    return {"product_id": product.id, "current_stock": product.stock, "predicted_stock": predicted_stock}
