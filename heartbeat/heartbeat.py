import requests

from .metrics import Metrics


class Heartbeat:

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def tick(self):
        metrics = Metrics.collect()
        try:
            response = requests.post(self.endpoint, json=metrics)
            response.raise_for_status()
            print(f"Heartbeat sent successfully: {response.status_code}")
        except requests.RequestException as e:
            print(f"Failed to send heartbeat: {e}")
