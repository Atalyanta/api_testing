from api.httpbin_api import http_bin_api
from http import HTTPStatus


def test_time_out():
    res = http_bin_api.time_out(5)      # пройти запрос на статус ответа за 5 сек.
    assert res.status_code == HTTPStatus.OK

def test_not_time():
    res = http_bin_api.time_out(2)
    assert not res[0]               #  вернется кортеж и false, ex, тк тест отработает за 3(так задано)
                                    # если этот тест упадет, будем смотреть res[1]