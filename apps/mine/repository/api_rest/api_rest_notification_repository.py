import requests
from django.conf import settings

from apps.mine.repository.notification_repository import INotificationRepository


class ApiRestNotificationRepository(INotificationRepository):
    _api_gateway = "https://wadaqrjsxk.execute-api.us-east-1.amazonaws.com"  # settings.API_GATEWAY_URL
    _api_token = settings.API_GATEWAY_TOKEN
    _path = "/development/notification/configuration"

    def save(self, setting):
        url = f"{self._api_gateway}{self._path}"
        request_data = requests.post(url, json=setting)
        if request_data.status_code == 201 or request_data.status_code == 200:
            return True
        return False

    def find_by_mine(self, mine_id, **kwargs):
        url = f"{self._api_gateway}{self._path}?mine={mine_id}"
        for key, value in kwargs.items():
            url += f"&{key}={value}"

        request_data = requests.get(url)
        if request_data.status_code == 200:
            json_response = request_data.json()
            return json_response
        return {}
