from django.urls import path

from apps.mine.views import Measurement, Alerts, Settings, zone_select

app_name = "mine"

urlpatterns = [
    path("measurement-site-select/<int:mine>", zone_select, name="measurement_site_select"),
    path("measurement/<int:mine>/<str:type_name>", Measurement.as_view(), name="measurement"),
    path("alerts/<int:mine>/<str:type_name>", Alerts.as_view(), name="alerts"),
    path("settings/<int:mine>/<str:type_name>", Settings.as_view(), name="settings"),
]
