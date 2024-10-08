# Geolocation API

SQLite for simplicity (use Postgres on production). You can delete one from repo and it will make new one.


## Description
The Geolocation API is a simple Django application that allows you to store geolocation data based on IP addresses or URLs. The API supports operations for adding, deleting, and retrieving geolocation data.

## Requirements
- Docker
- Docker Compose
- `curl` (for testing the API)

## How to Run the Application

1. **Clone the repository**:
   ```bash
   git clone https://github.com/paweljass/geoapp.git
2. **Docker build**:
- docker-compose up --build
- docker exec terminal: python manage.py makemigrations
- docker exec terminal: python manage.py migrate 


3. **Add geolocation with curl** (or Postman):
curl -X POST http://localhost:8000/api/geolocation/ -H "Content-Type: application/json" -d '{"ip_or_url": "7.7.7.7"}'

4. **Check added data**:
http://localhost:8000/api/geolocation/7.7.7.7/

<img width="325" alt="Zrzut ekranu 2024-10-8 o 10 21 53" src="https://github.com/user-attachments/assets/c69bfc0d-7dec-4a9c-bc62-747441fdc60d">


5. **Run tests**:
- docker exec terminal: python manage.py test

<img width="442" alt="Zrzut ekranu 2024-10-8 o 09 37 08" src="https://github.com/user-attachments/assets/96c35fac-cbc4-4e18-adfc-530830743026">












