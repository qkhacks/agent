from flask import Flask


class HealthApi:
    def __init__(self, app: Flask):
        self.app = app

    def register(self):
        @self.app.get("/health")
        def health():
            return {
                "status": "ok",
            }

        @self.app.get("/")
        def index():
            return {
                "agent": "silicate"
            }
