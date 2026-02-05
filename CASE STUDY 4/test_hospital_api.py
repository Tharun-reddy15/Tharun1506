import requests

BASE_URL = "http://127.0.0.1:6000"

def test_add_patient():
    payload = {
        "name": "Ravi",
        "age": 30,
        "gender": "Male"
    }
    response = requests.post(f"{BASE_URL}/patients", json=payload)
    assert response.status_code == 201