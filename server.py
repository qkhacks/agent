import os
from apscheduler.schedulers.background import BackgroundScheduler

from flask import Flask

from api import HealthApi
from heartbeat import Heartbeat

app = Flask(__name__)

HealthApi(app).register()

heartbeat = Heartbeat("https://silicate.requestcatcher.com/heartbeat")

scheduler = BackgroundScheduler()
scheduler.add_job(func=heartbeat.tick, trigger='interval', seconds=15)

if __name__ == '__main__':
    scheduler.start()
    app.run(
        host=os.getenv("HOST", '0.0.0.0'),
        port=int(os.getenv("PORT", "9876")),
        debug=os.getenv('DEBUG', True)
    )
