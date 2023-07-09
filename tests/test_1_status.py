import requests
from http import HTTPStatus


def test_1_status():
    url = 'http://reqres.in/api/users?page=2'
    response = requests.get(url)
    assert response.status_code == HTTPStatus.OK

