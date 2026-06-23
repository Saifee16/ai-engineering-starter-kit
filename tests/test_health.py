from fastapi.testclient import TestClient


def test_health_check(client: TestClient) -> None:
    response = client.get("/api/v1/health")

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True
    assert body["data"]["status"] == "ok"
    assert body["data"]["app"] == "AI Engineering Starter Kit"
    assert body["data"]["environment"] == "local"