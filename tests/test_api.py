from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

class TestClass:
    def test_health(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
    
    def test_list_items(self):
        response = client.get("/items")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        
