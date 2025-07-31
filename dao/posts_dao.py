import json

class PostsDAO:
    def __init__(self, path):
        self.path = path

    # Возвращает все посты
    def get_posts_all(self):
        with open(self.path, encoding="utf-8") as file:
            posts = json.load(file)

        return posts

    # Возвращает посты определенного пользователя
    def get_posts_by_user(self, user_name):
        with open(self.path, encoding="utf-8") as file:
            posts = json.load(file)

        result = []

        for post in posts:
            if post["poster_name"] == user_name:
                result.append(post)

        if len(result) == 0:
            raise ValueError ("У данного пользователя нет постов или некорректное имя пользователя")

        return result

    # Возвращает список постов по ключевому слову
    def search_for_posts(self, query):
        with open(self.path, encoding="utf-8") as file:
            posts = json.load(file)

        result = []

        for post in  posts:
            if query.lower() in post["content"].lower():
                result.append(post)

        if len(result) == 0:
            raise ValueError ("Нет поста с таким ключевым словом")

        return result

    # Возвращает один пост по его идентификатору
    def get_post_by_pk(self, pk):
        with open(self.path, encoding="utf-8") as file:
            posts = json.load(file)

        for post in posts:
            if post["pk"] == pk:
                return post

        raise ValueError("Поста с таким идентификатором не найдено")

    def get_post_by_tag(self, tag):
        with open(self.path, encoding="utf-8") as file:
            posts = json.load(file)

        result = []

        for post in posts:
            if tag.lower() in post["content"].lower():
                result.append(post)

        if len(result) == 0:
            raise ValueError("Не найдено постов по данному тегу")

        return result