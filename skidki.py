import shutil

import json


import requests
import xmltodict


def get_skidki_index(name_s):
    r = requests.get(
        f"http://app.lovesalesua.com/ua_offers_andr_1.xml"
    )
    o = xmltodict.parse(r.content)
    json.dumps(o)  # '{"e": {"a": ["text", "text"]}}'
    index = []
    for label1, offers in o.items():
        for label2, offer in offers.items():
            for discount in offer:
                if isinstance(discount, dict) \
                        and 'storeId' in discount \
                        and discount['storeId'] == name_s:
                    index.append(discount['numberOfPages'])
    return index


def get_skidki_name(name_s):
    r = requests.get(
        f"http://app.lovesalesua.com/ua_offers_andr_1.xml"
    )
    o = xmltodict.parse(r.content)
    json.dumps(o)  # '{"e": {"a": ["text", "text"]}}'
    name = []
    for label1, offers in o.items():
        for label2, offer in offers.items():
            for discount in offer:
                if isinstance(discount, dict) \
                        and 'storeId' in discount \
                        and discount['storeId'] == name_s:
                    name.append(discount['id'])
    return name
def get_additional_info(name_s):
    r = requests.get(
        f"http://app.lovesalesua.com/ua_offers_andr_1.xml"
    )
    o = xmltodict.parse(r.content)
    json.dumps(o)  # '{"e": {"a": ["text", "text"]}}'
    additionalInfo = []
    for label1, offers in o.items():
        for label2, offer in offers.items():
            for discount in offer:
                if isinstance(discount, dict) \
                        and 'storeId' in discount \
                        and discount['storeId'] == name_s:
                    additionalInfo.append(discount['additionalInfo'])
    return additionalInfo


def picture_skidki(index, name):
    url = 'http://app.lovesalesua.com/' + str(name) + '/image' + str(index) + '.jpg'
    r = requests.get(url, stream=True)
    r.raise_for_status()
    r.raw.decode_content = True  # support Content-Encoding e.g., gzip
    with open('picture.png', 'wb') as file:
        shutil.copyfileobj(r.raw, file)  # copy in chunks, it works for large files


def get_count_id(name_s):
    r = requests.get(
        f"http://app.lovesalesua.com/ua_offers_andr_1.xml"
    )
    o = xmltodict.parse(r.content)
    json.dumps(o)  # '{"e": {"a": ["text", "text"]}}'
    count = 0
    for label1, offers in o.items():
        for label2, offer in offers.items():
            for discount in offer:
                if isinstance(discount, dict) \
                        and 'storeId' in discount \
                        and discount['storeId'] == name_s:
                    count += 1
    return count