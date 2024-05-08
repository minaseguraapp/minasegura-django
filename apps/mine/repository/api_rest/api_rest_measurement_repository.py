import requests
from django.conf import settings

from apps.mine.repository.measurement_repository import IMeasurementRepository


class ApiRestMeasurementRepository(IMeasurementRepository):
    _api_gateway = settings.API_GATEWAY_URL
    _api_token = settings.API_GATEWAY_TOKEN
    _path = "/development/measurement"

    def save(self, measurement):
        url = f"{self._api_gateway}{self._path}"
        request_data = requests.post(url, json=measurement)
        if request_data.status_code == 201 or request_data.status_code == 200:
            return True
        return False

    def find_by_mine(self, mine_id, type_name, **kwargs):
        url = f"{self._api_gateway}{self._path}?mine={mine_id}"
        if type_name:
            url += f"&measurementType={type_name}"
        for key, value in kwargs.items():
            url += f"&{key}={value}"

        request_data = requests.get(url)
        if request_data.status_code == 200:
            json_response = request_data.json()
            return json_response['measurements']
        return []
