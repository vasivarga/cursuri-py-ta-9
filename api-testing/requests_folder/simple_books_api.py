import requests
from requests import Response

from requests_folder.generate_token_request import get_token

token = get_token()

def get_api_status():
    url = "https://simple-books-api.glitch.me/status"
    return requests.get(url)

def get_list_of_books(book_type="", limit=""):
    url = f"https://simple-books-api.glitch.me/books?type={book_type}&limit={limit}"
    return requests.get(url)

def get_book_by_id(book_id):
    url = f"https://simple-books-api.glitch.me/books/{book_id}"
    return requests.get(url)

def submit_order(book_id, customer_name):
    request_body = {
      "bookId": book_id,
      "customerName": customer_name
    }

    header_params = {
        'Authorization': f"Bearer {token}"
    }

    url = "https://simple-books-api.glitch.me/orders"

    return requests.post(url, headers=header_params, json=request_body)


def get_order(order_id):
    url = f"https://simple-books-api.glitch.me/orders/{order_id}"
    header_params = {
        'Authorization': f"Bearer {token}"
    }
    return requests.get(url, headers=header_params)

def update_order(order_id, new_customer_name):
    url = f"https://simple-books-api.glitch.me/orders/{order_id}"
    header_params = {
        'Authorization': f"Bearer {token}"
    }

    request_body = {
      "customerName": new_customer_name
    }

    return requests.patch(url, headers=header_params, json=request_body)

def delete_order(order_id):
    url = f"https://simple-books-api.glitch.me/orders/{order_id}"
    header_params = {
        'Authorization': f"Bearer {token}"
    }

    return requests.delete(url, headers=header_params)