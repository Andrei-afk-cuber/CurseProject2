# Skyprogram

Skyprogram is kind of Instagram, with posts and comments. The purpose of creating this application was to consolidate the acquired knowledge.

During development, views were created blueprints, containing views:
* main_blueprint
    * / - main page displaying all posts

* search_blueprint
    * /posts/<int:post_id> - page displaying post by post_id
    * /search/ - page displaying posts by root word
    * /users/<username> - page displaying posts by specific user

* api_blueprint
    * /api/posts/ - page displaying all posts in json format
    * /api/posts/<int:post_id> - page displaying post by post_id in json format