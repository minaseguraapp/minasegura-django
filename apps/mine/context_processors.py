from apps.mine.models import Mine
from apps.mine.repository.api_rest.api_rest_alert_repository import ApiRestAlertRepository


def get_user_mine(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        first_mine = Mine.objects.filter(manager=request.user).first()
        if first_mine:
            return {
                "user_mine": first_mine
            }
    return {
        "user_mine": None
    }


def get_alerts(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        alert_repository = ApiRestAlertRepository()
        mine = request.user.mines.all().first()
        alerts = alert_repository.find_by_mine(mine.id)
        alerts.sort(key=lambda x: x["alertTimestamp"], reverse=True)
        return {
            "alerts": alerts
        }
    return {
        "alerts": []
    }
