from api.register_api import api
from http import HTTPStatus
from utils.assertions import Assert


def test_create_hw():
    email = 'eve.holt@reqres.in'
    password = 'abcd'
    res = api.create_hw(email, password)

    assert res.status_code == HTTPStatus.CREATED
    assert res.json()['email'] == email
    assert res.json()['password'] == password

