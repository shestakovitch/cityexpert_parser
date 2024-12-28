import requests
from config import base_url, cookies, headers, params

def fetch_page(page: int):
    params["currentPage"] = str(page)
    response = requests.get(base_url, cookies=cookies, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"HTTP Error: {response.status_code}")

    return response.text
