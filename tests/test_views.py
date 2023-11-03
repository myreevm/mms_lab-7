from http import HTTPStatus


def test_index(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
