from flask import Blueprint, jsonify
from dao.posts_dao import PostsDAO

api_blueprint = Blueprint("api_blueprint", __name__)

post_dao = PostsDAO("data/data.json")

@api_blueprint.route("/posts")
def all_post_api_page():
    posts = post_dao.get_posts_all()
    return jsonify(posts)

@api_blueprint.route("/posts/<int:post_id>")
def post_by_id_api_page(post_id):
    post = post_dao.get_post_by_pk(post_id)
    return jsonify(post)