from django.urls import path

from apps.users.views import LoginFormView, login_user, logout_view, Dashboard

app_name = "users"

urlpatterns = [
    path("", LoginFormView.as_view(), name="login"),
    path("login-session", login_user, name="login_session"),
    path("logout", logout_view, name="logout"),
    path("dashboard/<int:mine>/", Dashboard.as_view(), name="dashboard")
]
