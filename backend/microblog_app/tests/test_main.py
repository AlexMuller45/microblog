from fastapi.testclient import TestClient

from main import app


def test_test():
    assert 1 == 1


def test_main():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}
