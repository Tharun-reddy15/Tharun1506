# -------------------------------
# API AUTOMATION USING PYTEST
# -------------------------------

import requests

BASE_URL = "http://127.0.0.1:5000"

def test_get_movies():
    response = requests.get(f"{BASE_URL}/movies")
    assert response.status_code == 200

def test_book_ticket():
    payload = {
        "movie": "Avatar",
        "show": "10:00 AM",
        "seats": 2
    }
    response = requests.post(f"{BASE_URL}/bookings", json=payload)
    assert response.status_code == 201