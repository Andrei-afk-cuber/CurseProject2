import pytest

data_for_test = [(1, 4), (2, 4), (3, 4), (4, 4), (5, 2), (6, 1), (7, 1)]

@pytest.mark.parametrize("input_data, expected_count", data_for_test)
def test_comments_dao(comments_dao, input_data, expected_count):
    # Проверка комментариев к посту 1
    comments = comments_dao.get_comments_by_post_id(input_data)
    assert len(comments) == expected_count, "Неверное кол-во комментариев для поста"

def test_comments_dao_value_error(comments_dao):
    with pytest.raises(ValueError):
        comments = comments_dao.get_comments_by_post_id(0)
    with pytest.raises(ValueError):
        comments = comments_dao.get_comments_by_post_id(9)