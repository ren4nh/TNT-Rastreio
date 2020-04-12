from flask import Flask
from flask_mail import Mail
import redis
import os

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'dc8efd96f2f4bc'
app.config['MAIL_PASSWORD'] = 'e64d7f270239ec'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)
redis_host = os.environ.get('REDISHOST', 'localhost')
redis_port = int(os.environ.get('REDISPORT', 6379))
redis = redis.StrictRedis(host=redis_host, port=redis_port)

from app import factory, handler, utils, routes