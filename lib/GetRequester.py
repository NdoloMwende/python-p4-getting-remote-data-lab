import requests
import json


class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.content  # ← RETURN BYTES, not .text

    def load_json(self):
        return json.loads(self.get_response_body())
    
if __name__ == "__main__":
    requester = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
    data = requester.load_json()