# -*- coding: utf-8 -*-
from app.handler import tnt
from app import redis as r
import json


def scrap(data):
    scraping = get_scraping(data['type'])
    key = data['email']
    json_data = json.dumps(data)
    r.sadd(key, json_data)
    return scraping.scrap(data)

def get_scraping(type):
    if type == 'TNT':
        return tnt.TntHandler()
    else:
        raise ValueError(type) 