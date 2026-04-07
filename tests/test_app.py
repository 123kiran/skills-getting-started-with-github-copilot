import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Arrange-Act-Assert: Test GET /activities

def test_get_activities():
    # Arrange: (nothing to arrange for this test)
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data

# Arrange-Act-Assert: Test POST /activities/{activity_name}/signup

def test_signup_for_activity():
    # Arrange
    activity = "Chess Club"
    email = "testuser@mergington.edu"
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert response.status_code == 200 or response.status_code == 400
    if response.status_code == 200:
        assert f"Signed up {email}" in response.json()["message"]
    else:
        assert response.json()["detail"] == "Already signed up for this activity"

# Arrange-Act-Assert: Test DELETE /activities/{activity_name}/participants/{email}

def test_remove_participant():
    # Arrange
    activity = "Chess Club"
    email = "testuser@mergington.edu"
    # Act
    response = client.delete(f"/activities/{activity}/participants/{email}")
    # Assert
    assert response.status_code == 200 or response.status_code == 404
    if response.status_code == 200:
        assert f"Removed {email}" in response.json()["message"]
    else:
        assert response.json()["detail"] == "Participant not found in this activity"
