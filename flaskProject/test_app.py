from app import app


def test_hello_world():
    app.config['TESTING'] = True
    client = app.test_client()
    result = client.get('/')
    assert result.data == b'Hello World!'
