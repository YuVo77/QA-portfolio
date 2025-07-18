import requests
from Automation.api_tests.endpoints.base_endpoint import Endpoint


class DeleteObject(Endpoint):


    def delete_by_id(self, object_id):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
        self.response_json = self.response.json()

