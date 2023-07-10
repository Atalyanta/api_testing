from api.httpbin_api import http_bin_api
from http import HTTPStatus
import re


def test_list_html():
    res = http_bin_api.list_html()      # обращаемся к апи, получаем ответ, записываем в res

    assert res.status_code == HTTPStatus.OK         # проверка на статус 200
    assert res.headers['Content-Type'] == 'text/html; charset=utf-8'    # проверка на заголовок


def test_robots():
    res = http_bin_api.robots_txt()
    assert res.status_code == HTTPStatus.OK
    assert res.headers['Content-Type'] == 'text/plain'
    assert re.fullmatch(r'.*User-agent: \*.*Disallow: /deny*', res.text, flags=re.DOTALL)

    # в теле должен быть текст User-agent: * Disallow: /deny
    # до него может быть ничего или любой текст
    # flags=re.DOTALL это переносы строк