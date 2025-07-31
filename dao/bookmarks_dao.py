import json

class BookmarksDAO:
    def __init__(self, path):
        self.path = path

    def load_bookmarks(self):
        with open(self.path, encoding="utf-8") as file:
            bookmarks = json.load(file)

        return bookmarks