from flask import Flask, request, make_response, jsonify
from flask_expects_json import expects_json
import json
import factory.scrapingfactory as sf
scraping = sf.ScrapingFactory()

app = Flask(__name__)

schema = {
    'type': 'object',
    'properties': {
        'identificacao': {'type': 'string'},
        'tipodoc': {'type': 'string'},
        'numdoc': {'type': 'string'},
        'type': {'type': 'string'}
    },
    'required': ['identificacao', 'numdoc', 'tipodoc', 'type']
}

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/', methods=['POST'])
@expects_json(schema)
def search_order():
    data = request.json
    return scraping.scrap(data)

@app.errorhandler(400)
def bad_request(error):
    print(error.description)
    return make_response(jsonify({'error': str(error.description)}), 400)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')    