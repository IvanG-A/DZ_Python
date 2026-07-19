import pytest
import requests


TOKEN = ""


@pytest.fixture(scope="session")
def api_client():
    if not TOKEN:
        pytest.skip("Токен не задан")
    base_url = "https://yougile.com/api-v2"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    return {"base_url": base_url, "headers": headers, "session": requests.Session()}


@pytest.fixture(scope="function")
def created_project_id(api_client):
    payload = {
        "title": f"Test Project {__import__('time').time_ns()}"
    }
    response = api_client["session"].post(
        f"{api_client['base_url']}/projects",
        json=payload,
        headers=api_client["headers"]
    )
    assert response.status_code == 201, "Не удалось создать проект"
    project_id = response.json()["id"]
    yield project_id