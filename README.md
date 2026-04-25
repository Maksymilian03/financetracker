# Finance Tracker
Aplikacja do zarządzania budżetem domowym pomagająca prowadzić miesięczny budżet oraz oszczędności.

## Technologie
- Django
- Django REST Framework

## Funkcjonalności
- Rejestracja i logowanie użytkowników
- Zarządzanie kategoriami wydatków
- Dodawanie transakcji (wydatki/przychody)
- Śledzenie inwestycji (akcje, ETF, obligacje)

## Instalacja
```bash
git clone https://github.com/Maksymilian03/financetracker
cd financetracker
python -m venv venv

# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Endpointy API
| Metoda | Endpoint | Opis |
|--------|----------|------|
| POST | /api/register/ | Rejestracja |
| POST | /api/login/ | Logowanie |
| GET/POST | /api/category/ | Kategorie |
| GET/POST | /api/transaction/ | Transakcje |
| GET/POST | /api/investment/ | Inwestycje |