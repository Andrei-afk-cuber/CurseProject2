from app import app
import pytest

data = [({"s":"Остров"}, "larry")]

@pytest.mark.parametrize("input_data, expected", data)
def test_search_blueprint(input_data, expected):
    response = app.test_client().get("/search", query_string=input_data, follow_redirects=True)
    assert response.status_code == 200, "Неверный статус-код для страницы поиска"
    assert f"{expected}".encode() in response.data

data_for_search_by_user = [("leo", "leo"), ("johnny", "johnny"), ("hank", "hank"), ("larry", "larry")]

@pytest.mark.parametrize("username, expected", data_for_search_by_user)
def test_posts_by_user(username, expected):
    response = app.test_client().get(f"/users/{username}")
    assert response.status_code == 200, "Неверный статус-код страницы"
    assert f"{expected}".encode() in response.data