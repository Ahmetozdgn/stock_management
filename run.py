# run.py
import uvicorn

if __name__ == "__main__":
    # "app.main:app" -> app klasöründeki main.py içindeki FastAPI app
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",   # Her yerden erişim için
        port=8000,        # Port numarası
        reload=True       # Kod değişirse otomatik yeniden başlatma
    )
