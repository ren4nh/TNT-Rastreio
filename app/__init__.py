from flask import Flask
from flask_mail import Mail
from apscheduler.schedulers.background import BackgroundScheduler
import redis
import os
import atexit

app = Flask(__name__)
app.config.from_pyfile('config.py')
mail = Mail(app)
redis_host = os.environ.get('REDISHOST', 'localhost')
redis_port = int(os.environ.get('REDISPORT', 6379))
redis = redis.StrictRedis(host=redis_host, port=redis_port)
scheduler = BackgroundScheduler(daemon=True)

from app.schedule import check

scheduler.add_job(func=check, trigger="cron", day_of_week="mon-fri", hour="8,14,18", minute=0, second=0)

scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

from . import routes, email, schedule