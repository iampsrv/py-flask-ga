from ap import app


def test_home1():
    response = app.test_client().get('/edit1')
    assert b"To Do App" in response.data
    assert b"Todo Title" in response.data
    assert b"Add" in response.data

