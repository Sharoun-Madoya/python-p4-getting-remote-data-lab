import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL ='https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
        response = requests.get(URL)
        return response.content

    def load_json(self):
        name_list = []

        names= json.loads(self.get_response_body())
        for name in names:
            name_list.append(name['name'])
            return names
        



















        
        #     response_body = self.get_response_body()
        # json_data = json.loads(response_body)
        # return json_data
