import random

import requests


def get_token():
    url = "https://simple-books-api.glitch.me/api-clients/"
    random_number = random.randint(1, 99999999999999999999)
    request_body = {
       "clientName": "Pycharm",
       "clientEmail": f'pyta9_{random_number}@google.com'
    }
    response = requests.post(url, json=request_body)
    token = response.json()['accessToken']
    return token
