from app import app
import pytest

def test_main_blueprint():
    response = app.test_client().get("/")
    assert response.status_code == 200, "Неверный статус код для главной страницы"

# Тестирование страницы с выводом постов по id
test_data = [(1, "leo"), (2, "johnny"), (3, "hank"), (4, "larry"), (5, "leo"), (6, "johnny"), (7, "hank"), (8, "larry")]

@pytest.mark.parametrize("post_id, expected", test_data)
def test_search_blueprint(post_id, expected):
    response = app.test_client().get(f"/posts/{post_id}")
    assert response.status_code == 200
    assert f"{expected}".encode() in response.data