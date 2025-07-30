from dao.posts_dao import PostsDAO
from dao.comments_dao import CommentsDAO
import pytest

@pytest.fixture()
def posts_dao():
    return PostsDAO("data/data.json")

@pytest.fixture()
def comments_dao():
    return CommentsDAO("data/comments.json")