from main import app
from fastapi.testclient import TestClient


def test_test():
    assert 1 == 1


def test_main():
    test_client = TestClient(app)

    response = test_client.get("/")
    assert response.status_code == 200

    data = response.json()
    assert data["message"] == "Hello world!"
