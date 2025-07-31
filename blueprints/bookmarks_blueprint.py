from flask import Blueprint, render_template

bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__)

@bookmarks_blueprint.route("/")
def bookmarks_index_page():
    return render_template("bookmarks.html")

@bookmarks_blueprint.route("/add/postid")
def add_bookmarks_page():
    return render_template("bookmarks.html")

@bookmarks_blueprint.route("/remove/postid")
def remove_bookmarks_page():
    return render_template()