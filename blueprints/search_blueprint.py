from flask import Blueprint, render_template, request

from dao.posts_dao import PostsDAO
from dao.comments_dao import CommentsDAO

search_blueprint = Blueprint("post_blueprint", __name__)

post_dao = PostsDAO("data/data.json")
comments_dao = CommentsDAO("data/comments.json")

# Вывод поста по его id
@search_blueprint.route("/posts/<int:post_id>")
def post(post_id):
    search_post = post_dao.get_post_by_pk(post_id)
    comments = comments_dao.get_comments_by_post_id(post_id)
    return render_template("post.html", post=search_post, comments=comments, comments_len = len(comments))

# Вывод постов по ключевому слову
@search_blueprint.route("/search/")
def search_post_by_query():
    s = request.args.get("s")
    posts = post_dao.search_for_posts(s)
    return render_template("search.html", query=s, posts_count=len(posts), posts=posts)

# Вывод постов определенного пользователя
@search_blueprint.route("/users/<username>")
def posts_by_user(username):
    posts = post_dao.get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts, posts_count=len(posts))