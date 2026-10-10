from fastapi.testclient import TestClient

from distrirag.api.main import app

client = TestClient(app)


def test_health_ready_returns_200():
    response = client.get("/health/ready")
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ready"
    assert "version" in data
