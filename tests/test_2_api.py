from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert
import re


def test_list_users():
    res = api.list_users()
    assert res.status_code == HTTPStatus.OK
#   Assert.validate_schema(res.json())
    assert res.headers['Cache-Control'] == 'max-age=14400'      #  проверка заголовка


def test_single_user_not_found():
    res = api.single_user_not_found()

    assert res.status_code == HTTPStatus.NOT_FOUND
  #  Assert.validate_schema(res.json())


def test_single_user():
    res = api.single_user()
    res_body = res.json()

    assert res.status_code == HTTPStatus.OK
#    Assert.validate_schema(res_body)

    assert res_body['data']['first_name'] == 'Janet'
    example = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }

    assert example == res_body

    assert re.fullmatch(r'\w+', res_body['data']['last_name'])  # проверка на то, что несколько букв
                    # r - рег.выражение, \w+ - буквы, несколько
    assert re.fullmatch(r'\w[a-z]{5}', res_body['data']['last_name'])   # от а до z и 6 букв
    assert re.fullmatch(r'\w[a-z]+', res_body['data']['last_name'])     # буквы от а до z, 1 и более
    assert re.fullmatch(r'.+', res_body['data']['last_name'])   # любые символы


def test_created():
    res = api.create()

    assert res.status_code == HTTPStatus.CREATED
 #   Assert.validate_schema(res.json())


def test_create():      # внеси данные в базу
    name = 'Boris'
    job = 'Tester'
    res = api.create(name, job)

    assert res.status_code == HTTPStatus.CREATED
    assert res.json()['name'] == name
    assert res.json()['job'] == job

    assert re.fullmatch(r'\d{1,4}', res.json()['id'])   # проверка, что id соотв.паттерну: числа от 1 до4

    assert api.delete_user(res.json()['id']).status_code == HTTPStatus.NO_CONTENT
                # после проверки удаляем то, что внесли

