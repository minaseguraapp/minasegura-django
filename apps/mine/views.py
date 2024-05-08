import datetime
import enum

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from apps.mine.choices import MeasurementSiteChoice
from apps.mine.models import Zone
from apps.mine.repository.api_rest.api_rest_measurement_repository import ApiRestMeasurementRepository
from apps.mine.repository.api_rest.api_rest_notification_repository import ApiRestNotificationRepository
from apps.mine.repository.api_rest.api_rest_settings_repository import ApiRestSettingsRepository

MEASUREMENT_TYPE = {
    "gas": "METHANE",
    "coal": "COAL_DUST"
}


class MeasurementTypeEnum(enum.Enum):
    GAS = "gas"
    COAL = "coal"


class Measurement(LoginRequiredMixin, View):
    repository = ApiRestMeasurementRepository()
    measurement_site_choice = MeasurementSiteChoice.choices

    def get(self, request, mine: int, type_name: str, *args, **kwargs):
        measurement_list = self.repository.find_by_mine(mine,
                                                        MEASUREMENT_TYPE.get(type_name), **kwargs)
        return render(
            request,
            self.get_template(type_name),
            {
                "type_name": type_name,
                "measurement_site_choice": self.measurement_site_choice,
                "measurement_list": measurement_list,
            },
        )

    def post(self, request, mine: int, type_name: str, *args, **kwargs):
        data = request.POST.copy()
        data["mine"] = mine
        save_result = False
        if type_name == MeasurementTypeEnum.GAS.value:
            measurement_data = self.parse_data_methane(data)
            save_result = self.repository.save(measurement_data)
        if type_name == MeasurementTypeEnum.COAL.value:
            measurement_data = self.parse_data_coal_dust(data)
            save_result = self.repository.save(measurement_data)

        if save_result:
            messages.success(request, "Medición guardada correctamente")
        else:
            messages.error(request, "Error al guardar la medición")
        return redirect('mine:measurement', mine=mine, type_name=type_name)

    @staticmethod
    def get_template(type_name: str):
        return f"mine/{type_name}/measurement.html"

    @staticmethod
    def parse_data_methane(post_data):
        zone = Zone.objects.get(id=post_data.get("zone"))
        present_date = datetime.datetime.now()
        timestamp = datetime.datetime.timestamp(present_date)
        data = {
            "timestamp": timestamp,
            "measurementType": "METHANE",
            "zone": {
                "id": zone.id,
                "type": zone.zone_type.name,
                "mine": {
                    "id": post_data.get("mine"),
                }
            },
            "measurementInfo": {
                "measurementSite": post_data.get("measurement_site"),
                "methaneLevel": post_data.get("methane_level"),
            }
        }
        return data

    @staticmethod
    def parse_data_coal_dust(post_data):
        zone = Zone.objects.get(id=post_data.get("zone"))
        present_date = datetime.datetime.now()
        timestamp = datetime.datetime.timestamp(present_date)
        data = {
            "timestamp": timestamp,
            "measurementType": "COAL_DUST",
            "zone": {
                "id": zone.id,
                "type": zone.zone_type.name,
                "mine": {
                    "id": post_data.get("mine"),
                }
            },
            "measurementInfo": {
                "dustLevel": post_data.get("dust_level"),
                "particleSize": post_data.get("particle_size"),
            }
        }
        return data


class Alerts(LoginRequiredMixin, View):

    def get(self, request, mine: int, type_name: str):
        template_name = self.get_template(type_name)
        return render(
            request,
            template_name,
            {
                "type_name": type_name,
            },
        )

    @staticmethod
    def get_template(type_name: str):
        return f"mine/{type_name}/alerts.html"


class Settings(LoginRequiredMixin, View):
    repository = ApiRestSettingsRepository()
    notification_repository = ApiRestNotificationRepository()

    def get(self, request, mine: int, type_name: str, *args, **kwargs):
        template_name = self.get_template(type_name)
        settings_list = self.repository.find_by_mine(mine)
        settings = None
        if type_name == MeasurementTypeEnum.GAS.value:
            settings = next(setting for setting in settings_list if setting["measurementType"] == "METHANE")
        if type_name == MeasurementTypeEnum.COAL.value:
            settings = next(setting for setting in settings_list if setting["measurementType"] == "COAL_DUST")

        notification_settings = self.notification_repository.find_by_mine(mine)

        return render(
            request,
            template_name,
            {
                "type_name": type_name,
                "settings": settings,
                "notification_settings": notification_settings,
            },
        )

    def post(self, request, mine: int, type_name: str, *args, **kwargs):
        data = request.POST.copy()
        data["mine"] = mine
        save_result = False
        if type_name == MeasurementTypeEnum.GAS.value:
            measurement_data = self.parse_data_methane(data)
            save_result = self.repository.save(measurement_data)
        if type_name == MeasurementTypeEnum.COAL.value:
            measurement_data = self.parse_data_coal_dust(data)
            save_result = self.repository.save(measurement_data)

        notification_data = self.parse_notification_data(data)
        save_notification_result = self.notification_repository.save(notification_data)

        if save_notification_result:
            messages.success(request, "Configuración de notificaciones guardada correctamente")
        else:
            messages.error(request, "Error al guardar la configuración de notificaciones")

        if save_result:
            messages.success(request, "Configuración de alertas guardada correctamente")
        else:
            messages.error(request, "Error al guardar la configuración de alertas")
        return redirect('mine:settings', mine=mine, type_name=type_name)

    @staticmethod
    def get_template(type_name: str):
        return f"mine/{type_name}/settings.html"

    @staticmethod
    def parse_data_methane(post_data):
        present_date = datetime.datetime.now()
        timestamp = datetime.datetime.timestamp(present_date)
        data = {
            "timestamp": timestamp,
            "measurementType": "METHANE",
            "mineId": post_data.get("mine"),
            "thresholdInfo": {
                "miningOperationsMaxMethaneLevel": post_data.get("mining_operations_max_methane_level"),
                "mainAirReturnMaxMethaneLevel": post_data.get("main_air_return_max_methane_level"),
                "airReturnFromStallsMaxMethaneLevel": post_data.get("air_return_from_stalls_max_methane_level"),
                "airReturnFromPrepAndDevMaxMethaneLevel": post_data.get(
                    "air_return_from_prep_and_dev_max_methane_level"),
            }
        }
        return data

    @staticmethod
    def parse_data_coal_dust(post_data):
        present_date = datetime.datetime.now()
        timestamp = datetime.datetime.timestamp(present_date)
        data = {
            "timestamp": timestamp,
            "measurementType": "COAL_DUST",
            "mineId": post_data.get("mine"),
            "thresholdInfo": {
                "maxDustLevel": post_data.get("max_dust_level"),
                "maxParticleSize": post_data.get("max_particle_size"),
            }
        }
        return data

    @staticmethod
    def parse_notification_data(post_data):
        present_date = datetime.datetime.now()
        timestamp = datetime.datetime.timestamp(present_date)
        data = {
            "mineId": str(post_data.get("mine")),
            "timestamp": int(timestamp),
            "notificationInfo": {
                "email": post_data.get("email"),
                "cellphone": post_data.get("cellphone"),
            }
        }
        return data


def zone_select(request, mine: int):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            list_zone = Zone.objects.filter(Q(name__icontains=query) | Q(code__icontains=query)).values('id',
                                                                                                        'name')
            return JsonResponse({"zones": list(list_zone)})
    return JsonResponse({"zones": []})
