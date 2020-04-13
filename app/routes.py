from flask import Flask, request, make_response, jsonify
from flask_expects_json import expects_json
import json
from app import app, factory, redis
scraping = factory.scrapingfactory.ScrapingFactory()

schema = {
    'type': 'object',
    'properties': {
        'identificacao': {'type': 'string'},
        'tipodoc': {'type': 'string'},
        'numdoc': {'type': 'string'},
        'type': {'type': 'string'},
        'email': {'type': 'string'}
    },
    'required': ['identificacao', 'numdoc', 'tipodoc', 'type', 'email']
}

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/redis')
def get_redis_keys():
    return str(redis.keys('*'))

@app.route('/redis/<key>')
def get_redis_set(key):
    return str(redis.smembers(key))

@app.route('/', methods=['POST'])
@expects_json(schema)
def search_order():
    data = request.json
    return scraping.scrap(data)

@app.errorhandler(400)
def bad_request(error):
    print(error.description)
    return make_response(jsonify({'error': str(error.description)}), 400)