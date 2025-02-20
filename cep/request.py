import requests

class Request:
    def __init__(self, url):
        self.url = url

    def get(self):
        response = requests.get(self.url)
        return response.json()
