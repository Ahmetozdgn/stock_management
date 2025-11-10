# 🏪 Stock Management API
Stock Management API, FastAPI + SQLite ile geliştirilmiş basit bir stok yönetim sistemidir. Proje, kullanıcı kayıt & login (JWT), ürün ekleme/listeleme, stok artırma/azaltma ve basit AI stok tahmini özelliklerini içerir. Swagger dokümantasyonu ile tüm endpoint’ler kolayca test edilebilir.

## 🚀 Öne Çıkan Özellikler
- Kullanıcı kayıt & login (JWT)
- Ürün ekleme / listeleme
- Stok artırma / azaltma
- Basit AI stok tahmini
- Swagger dokümantasyonu ile anında test

## 🧰 Kurulum ve Çalıştırma
```bash
# Depoyu klonla ve klasöre gir
git clone https://github.com/Ahmetozdgn/stock_management.git
cd stock_management

# Paketleri yükle
pip install -r requirements.txt

# API’yi başlat
python run.py
Sunucu çalıştıktan sonra tarayıcıdan http://127.0.0.1:8000/docs
 adresine giderek tüm endpoint’leri tek tıkla test edebilirsiniz.

### 5️⃣ Proje yapısı

```markdown
## 📂 Proje Yapısı
- `app/` → Modeller, endpointler, veritabanı işlemleri
- `run.py` → API başlatma dosyası
- `requirements.txt` → Kullanılan paketler
- `stock.db` → SQLite veritabanı
