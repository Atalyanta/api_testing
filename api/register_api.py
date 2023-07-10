from api.client import Client
import json


class ApiReg(Client):
    USERS = '/users'
    BASE_URL = 'https://reqres.in/api/register'

    def create_hw(self, name: str, job: str):
        """
        :method:    post
        :routs:     /api/users
        :status:    200
        :body:      {
                        "email": "",
                        "password": ""
                     }
        """

        url = self.BASE_URL + self.USERS
        payload = json.dumps({
        "email": F"{email}",
        "password": F"{password}"
        })
        headers = {
        'Content-Type': 'application/json'
        }
        return self.post(url, headers, payload)


api = ApiReg()