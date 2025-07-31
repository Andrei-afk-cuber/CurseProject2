import pytest

def test_bookmarks_load(bookmarks_dao):
    bookmarks = bookmarks_dao.load_bookmarks()
    assert type(bookmarks) == list, "Неверный тип возвращаемого значения"