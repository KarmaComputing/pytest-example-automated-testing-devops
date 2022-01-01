from app import app


def test_add():
    assert app.add(1, 1) == 2
