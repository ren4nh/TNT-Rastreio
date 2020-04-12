from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'dc8efd96f2f4bc'
app.config['MAIL_PASSWORD'] = 'e64d7f270239ec'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

from app import factory, handler, utils, routes