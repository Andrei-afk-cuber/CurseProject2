from flask import Blueprint, render_template
from dao.posts_dao import PostsDAO

main_blueprint = Blueprint("main_blueprint", __name__)

post_dao = PostsDAO("data/data.json")

@main_blueprint.route("/")
def index_page():
    posts = post_dao.get_posts_all()
    return render_template("index.html", posts=posts)