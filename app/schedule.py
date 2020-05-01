# -*- encoding: utf-8 -*-
from app import redis, scheduler
from app.factory.scrapingfactory import scrap
import json

def check():
    for key in redis.keys('*'):
        for data in redis.smembers(key):
            data = data.decode('utf-8')
            scrap(json.loads(data))

