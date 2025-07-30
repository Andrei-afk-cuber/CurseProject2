import pytest
from app import app
import json

def test_all_posts_blueprint(posts_dao):
    response = app.test_client().get("/api/posts")
    assert type(response.json) == list, f"Неверный тип возвращаемого объекта"
    assert response.json == posts_dao.get_posts_all()

test_data = (1, 2, 3, 4, 5, 6, 7, 8)

@pytest.mark.parametrize("pk", test_data)
def test_post_by_id(posts_dao, pk):
    response = app.test_client().get(f"/api/posts/{pk}")
    assert response.json == posts_dao.get_post_by_pk(pk)
    assert type(response.json) == dict, "Неверный тип возвращаемого объекта"