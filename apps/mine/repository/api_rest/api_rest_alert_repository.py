import requests
from django.conf import settings

from apps.mine.repository.alert_repository import IAlertRepository


class ApiRestAlertRepository(IAlertRepository):
    _api_gateway = "https://d7rqzryrjk.execute-api.us-east-1.amazonaws.com"  # settings.API_GATEWAY_URL
    _api_token = settings.API_GATEWAY_TOKEN
    _path = "/development/alert"

    def find_by_mine(self, mine_id):
        url = f"{self._api_gateway}{self._path}?mine={mine_id}"
        request_data = requests.get(url)
        if request_data.status_code == 200:
            json_response = request_data.json()
            return json_response['alerts']
        return []
