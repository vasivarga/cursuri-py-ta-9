import requests
from requests import Response


def get_api_status():
    url = "https://simple-books-api.glitch.me/status"
    return requests.get(url)

def get_list_of_books():
    url = "https://simple-books-api.glitch.me/books"
    return requests.get(url)