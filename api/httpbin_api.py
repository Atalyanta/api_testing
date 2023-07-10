from api.client import Client


class HttpBinApi(Client):
    HTML = '/html'
    BASE_URL = 'https://httpbin.org'
    ROBOTS = '/robots.txt'
    TIME = "/delay"

    def list_html(self):
        """                         #  зеленый блок ниже - инфа для себя, можно не писать
        :method:    get             # это то, что должно быть в ответе
        :routs:     /html
        :status:    200
        """
        url = self.BASE_URL + self.HTML
        return self.get(url)


    def robots_txt(self):
        """
             :method:    get
             :routs:     /robots.txt
             :status:    200
        """
        url = self.BASE_URL + self.ROBOTS
        return self.get(url)


    def time_out(self, delay=1):            #
        """
        :method:    get
        :routs:     /delay/{delay}
        :status:    200
        """
        url = self.BASE_URL + self.TIME + f'/3'     # запрос отработает через 3, это можно менять
        try:                                        # делаем запрос в урл,по умолчанию тест упадет,потому что 1 меньше 3
            return self.get(url, timeout=delay)     #
        except Exception as ex:
            return False, ex


http_bin_api = HttpBinApi()
