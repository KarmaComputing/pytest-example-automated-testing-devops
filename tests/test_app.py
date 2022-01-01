from app import app


def test_add():
    assert app.add(1, 1) == 2


def test_get_api_key():
    assert app.get_api_key() is not None
