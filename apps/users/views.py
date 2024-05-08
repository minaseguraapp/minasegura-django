from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from apps.inventory.models import Maintenance
from apps.mine.models import Mine


@login_required(login_url=reverse_lazy("user:login"), redirect_field_name=None)
def login_user(request):
    if request.user.is_superuser:
        return redirect(reverse_lazy("admin:index"))

    first_mine = Mine.objects.filter(manager=request.user).first()
    if not first_mine:
        messages.error(request, "¡No tienes minas asignadas!")
        return redirect(reverse_lazy("user:logout"))
    return redirect(reverse_lazy("users:dashboard", kwargs={"mine": first_mine.id}))


@login_required(login_url=reverse_lazy("users:login"), redirect_field_name=None)
def logout_view(request):
    logout(request)
    return redirect(reverse_lazy("users:login"))


class LoginFormView(TemplateView):
    template_name = "users/login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy("user:login_session"))
        return render(request, self.template_name, {})

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
        else:
            messages.error(request, "¡Nombre de usuario o contraseña incorrectos!")
        return redirect(reverse_lazy("user:login_session"))


class Dashboard(LoginRequiredMixin, View):
    template_name = "users/dashboard.html"

    def get(self, request, mine: int, *args, **kwargs):
        last_maintenance = self.get_week_maintenance(request, mine)
        return render(
            request,
            self.template_name,
            {
                "maintenance_list": last_maintenance,
            },
        )

    @staticmethod
    def get_week_maintenance(request, mine: int, *args, **kwargs):
        maintenance_list = Maintenance.objects.filter(equipment__mine_id=mine)[:5]
        return maintenance_list
