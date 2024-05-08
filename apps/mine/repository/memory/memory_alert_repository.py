from apps.mine.repository.alert_repository import IAlertRepository


class MemoryAlertRepository(IAlertRepository):

    def __init__(self):
        self._alerts = []

    def save(self, alert):
        self._alerts.append(alert)

    def find_all(self):
        return self._alerts
