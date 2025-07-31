from flask import Blueprint, render_template
from dao.posts_dao import PostsDAO

tag_blueprint = Blueprint("tag_blueprint", __name__)

post_dao = PostsDAO("data/data.json")

@tag_blueprint.route("/tag/<tagname>")
def index_tag_page(tagname):
    posts = post_dao.get_post_by_tag(tagname)
    return render_template("tag.html", )