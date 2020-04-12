from app.handler import tnt
from app import redis as r
import json

class ScrapingFactory:
    def scrap(self, data):
        scraping = get_scraping(data['type'])
        key = data['email']
        r.rpush(key, json.dumps(data))
        print(r.lrange(key, 0, -1))
        return scraping.scrap(data)

def get_scraping(type):
    if type == 'TNT':
        return tnt.TntHandler()
    else:
        raise ValueError(type) 