
def test_flask_api(client):
    resp = client.get('/api/heroes')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data[1] == {'name': 'Narco', 'Birth': 'Mon, 23 Apr 1984 00:00:00 GMT', 'id': 12}
    assert data[4] == {'name': 'Magneta', 'Birth': 'Tue, 09 Dec 1980 00:00:00 GMT', 'id': 15}
    assert data[6] == {'name': 'Dynama', 'Birth': 'Sat, 08 Feb 1992 00:00:00 GMT', 'id': 17}


def test_flask_api_regression(client, data_regression):
    resp = client.get('/api/heroes')
    assert resp.status_code == 200
    data_regression.check(resp.get_json())


def test_flask_api_regression_collection(client, data_regression):
    resp = client.get('/api/heroes')
    assert resp.status_code == 200
    data_regression.check(resp.get_json())

    resp = client.get('/api/heroes/14')
    assert resp.status_code == 200
    data_regression.check(
        resp.get_json(),
        basename='test_flask_api_item'
    )
