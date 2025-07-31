from flask import Flask

# Импорт блюпринтов
from blueprints.main_blueprint import main_blueprint
from blueprints.search_blueprint import search_blueprint
from blueprints.api_blueprints import api_blueprint
from blueprints.tag_blueprint import tag_blueprint
from blueprints.bookmarks_blueprint import bookmarks_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(api_blueprint, url_prefix="/api")
app.register_blueprint(tag_blueprint)
app.register_blueprint(bookmarks_blueprint, url_prefix="/bookmarks")

@app.errorhandler(404)
def not_found_error(error):
    return "Страница не найдена"

@app.errorhandler(500)
def server_international_error(error):
    return "Произошли ошибки на стороне сервера"

if __name__ == "__main__":
    app.run()