import shutil

import requests
import json


def get_len_data(data):
    return len(data['products'])


def get_data():
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/83.0.4103.97 Safari/537.36"}
    r = requests.get(
        f"https://www.atbmarket.com/api2/catalogue/product-list/?type=1", headers=headers

    )
    try:
        r.raise_for_status()
    finally:
        data = r.json()
        return data


def picture(url):
    r = requests.get(url, stream=True)
    r.raise_for_status()
    r.raw.decode_content = True  # support Content-Encoding e.g., gzip
    with open('picture.png', 'wb') as file:
        shutil.copyfileobj(r.raw, file)  # copy in chunks, it works for large files
