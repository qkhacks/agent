import os

from flask import Flask

from api import HealthApi

app = Flask(__name__)

HealthApi(app).register()

if __name__ == '__main__':
    app.run(
        host=os.getenv("HOST", '0.0.0.0'),
        port=int(os.getenv("PORT", "9876")),
        debug=os.getenv('DEBUG', True)
    )
