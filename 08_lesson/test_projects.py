import requests
import time


# ---------- ПОЗИТИВНЫЕ ТЕСТЫ ----------

def test_create_project(api_client):
    """POST /projects: успешное создание проекта"""
    unique_title = f"New Project {time.time_ns()}"
    payload = {"title": unique_title}
    response = api_client["session"].post(
        f"{api_client['base_url']}/projects",
        json=payload,
        headers=api_client["headers"]
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    project_id = data["id"]

    # Проверяем, что проект создался с правильным названием
    get_resp = api_client["session"].get(
        f"{api_client['base_url']}/projects/{project_id}",
        headers=api_client["headers"]
    )
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == unique_title


def test_get_project(api_client, created_project_id):
    """GET /projects/{id}: получение существующего проекта"""
    project_id = created_project_id
    response = api_client["session"].get(
        f"{api_client['base_url']}/projects/{project_id}",
        headers=api_client["headers"]
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id
    assert "title" in data


def test_update_project(api_client, created_project_id):
    """PUT /projects/{id}: обновление названия проекта"""
    project_id = created_project_id
    new_title = f"Updated {time.time_ns()}"
    payload = {"title": new_title}
    response = api_client["session"].put(
        f"{api_client['base_url']}/projects/{project_id}",
        json=payload,
        headers=api_client["headers"]
    )
    assert response.status_code == 200

    # Проверяем, что изменения сохранились
    get_resp = api_client["session"].get(
        f"{api_client['base_url']}/projects/{project_id}",
        headers=api_client["headers"]
    )
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == new_title


# ---------- НЕГАТИВНЫЕ ТЕСТЫ ----------

def test_create_project_invalid_data(api_client):
    """POST /projects: ошибка при отсутствии обязательного поля title"""
    payload = {}
    response = api_client["session"].post(
        f"{api_client['base_url']}/projects",
        json=payload,
        headers=api_client["headers"]
    )
    assert response.status_code in [400, 422]


def test_get_project_not_found(api_client):
    """GET /projects/{id}: ошибка при запросе несуществующего проекта"""
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = api_client["session"].get(
        f"{api_client['base_url']}/projects/{fake_id}",
        headers=api_client["headers"]
    )
    assert response.status_code == 404


def test_update_project_not_found(api_client):
    """PUT /projects/{id}: ошибка при обновлении несуществующего проекта"""
    fake_id = "00000000-0000-0000-0000-000000000000"
    payload = {"title": "Any Title"}
    response = api_client["session"].put(
        f"{api_client['base_url']}/projects/{fake_id}",
        json=payload,
        headers=api_client["headers"]
    )
    assert response.status_code == 404


def test_unauthorized():
    """Проверка, что запрос без токена возвращает 401"""
    client = requests.Session()
    response = client.get("https://yougile.com/api-v2/projects")
    assert response.status_code == 401