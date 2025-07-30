import json

from dao.posts_dao import PostsDAO

class CommentsDAO:
    def __init__(self, path):
        self.path = path

    # Возвращает комментарии определенного поста
    def get_comments_by_post_id(self, post_id):
        with open(self.path, encoding="utf-8") as file:
            comments = json.load(file)

        posts = PostsDAO("data/data.json").get_posts_all()

        if post_id < 1 or post_id > len(posts):
            raise ValueError

        result = []

        for comment in comments:
            if comment["post_id"] == post_id:
                result.append(comment)


        return result