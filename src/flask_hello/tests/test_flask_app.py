
def test_flask_hello(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert "Hello Flask Conf" in resp.data.decode()


def test_flask_hello_regression(client, file_regression):
    resp = client.get('/')
    assert resp.status_code == 200
    file_regression.check(resp.data.decode(), extension=".html")




# gitpitch
