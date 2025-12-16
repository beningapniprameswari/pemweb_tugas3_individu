# Product Review Analyzer

Aplikasi backend untuk menganalisis sentimen dan key points dari ulasan produk menggunakan Google Gemini API, lalu menyimpannya ke database PostgreSQL. 

## Tech Stack
- FastAPI
- SQLAlchemy
- PostgreSQL (pgAdmin 4)
- Google Gemini API
- Python 3.10+

## Setup

### Aktifkan Virtual Environment
```bash
venv\Scripts\activate
```

### Install Dependency
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv google-generativeai
```

### Konfigurasi Database
- Buat database menggunakan pgAdmin 4:
```bash
CREATE DATABASE reviewdb;
```
- Buat file .env di folder backend/:
```bash
DATABASE_URL=postgresql://postgres:PASSWORD@localhost:5432/reviewdb
GEMINI_API_KEY=API_KEY_KAMU
```

- Buat tabel (jalankan sekali):
bash``
Copy code
python
```
```bash
Copy code
from database import Base, engine
from models import Review

Base.metadata.create_all(bind=engine)
```

### Menjalankan Aplikasi
```bash
uvicorn main:app --reload
```

### Akses:
API: http://127.0.0.1:8000
Docs: http://127.0.0.1:8000/doc

### Endpoint API
POST /api/analyze-review

GET /api/reviews











