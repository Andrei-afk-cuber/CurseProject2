import pytest

# Тестирование метода для получения всех постов
def test_get_posts_all(posts_dao):
    posts = posts_dao.get_posts_all()
    assert type(posts) == list, "Неверный тип возвращаемого объекта"
    assert len(posts) == 8, "Неверная длина возвращаемого объекта"
    assert tuple(posts[0].keys()) == ("poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count",
                                      "pk"), f"Неверные ключи в словаре {posts[0].keys()}"

# Тест метода для получения поста по имени пользователя
tests_result = [("johnny", 2), ("leo", 2), ("hank", 2), ("larry", 2)]

@pytest.mark.parametrize("user_name, posts_count", tests_result)
def test_get_posts_by_user(posts_dao, user_name, posts_count):
    posts = posts_dao.get_posts_by_user(user_name)
    assert type(posts) == list, "Неверный тип возвращаемого объекта"
    assert tuple(posts[0].keys()) == ("poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count",
                                      "pk"), f"Неверные ключи в словаре {posts[0].keys()}"
    assert len(posts) == posts_count, "Неверное количество возвращаемых постов"

@pytest.mark.parametrize("user_name, expected", [("Andrei", ValueError), ("Picture", ValueError)])
def test_get_posts_by_user_value_error(posts_dao, user_name, expected):
    with pytest.raises(expected):
        posts = posts_dao.get_posts_by_user(user_name)

# Тестирование получение поста по идентификатору
data_for_post_by_pk_test = [(1, "leo"), (2, "johnny"), (3, "hank"), (4, "larry"), (5, "leo"), (6, "johnny"), (7, "hank"), (8, "larry")]

@pytest.mark.parametrize("pk, poster_name", data_for_post_by_pk_test)
def test_get_posts_by_pk(posts_dao, pk, poster_name):
    post = posts_dao.get_post_by_pk(pk)
    assert type(post) == dict, "Неверный тип возвращаемого объекта (ожидался dict)"
    assert post["poster_name"] == poster_name
    assert list(post.keys()) == ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count",
                                      "pk"], f"Неверные ключи в словаре {list(post.keys())}"

@pytest.mark.parametrize("input_data, expected", [(0, ValueError), (10, ValueError)])
def test_get_posts_by_pk_value_error(posts_dao, input_data, expected):
    with pytest.raises(expected):
        post = posts_dao.get_post_by_pk(input_data)

# Тестирование метода для поиска постов по ключевому слову
data_for_test_query_search = [("О", 8), ("о", 8), ("Острова", 1)]

@pytest.mark.parametrize("search_word, count_of_posts", data_for_test_query_search)
def test_get_posts_by_query(posts_dao, search_word, count_of_posts):
    posts = posts_dao.search_for_posts(search_word)
    assert type(posts) == list, "Неверный тип возвращаемого объекта"
    assert len(posts) == count_of_posts, "Не совпадения кол-ва постов"