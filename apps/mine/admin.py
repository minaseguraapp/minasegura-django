import datetime

from django.contrib import admin

from .models import Mine, Zone, ZoneType
from .repository.api_rest.api_rest_settings_repository import ApiRestSettingsRepository


@admin.register(Mine)
class MineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'manager')
    search_fields = ('name', 'description', 'manager__username')
    list_filter = ('manager',)

    repository = ApiRestSettingsRepository()

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        mine_id = obj.id
        get_mine = self.repository.find_by_mine(mine_id)
        if not get_mine:
            self.repository.save(self.parse_data_methane(mine_id))
            self.repository.save(self.parse_data_coal_dust(mine_id))

    @staticmethod
    def parse_data_methane(mine_id):
        present_date = datetime.datetime.now()
        timestamp = datetime.datetime.timestamp(present_date)
        data = {
            "timestamp": timestamp,
            "measurementType": "METHANE",
            "mineId": mine_id,
            "thresholdInfo": {
                "miningOperationsMaxMethaneLevel": "1.0",
                "mainAirReturnMaxMethaneLevel": "1.0",
                "airReturnFromStallsMaxMethaneLevel": "1.0",
                "airReturnFromPrepAndDevMaxMethaneLevel": "1.5"
            }
        }
        return data

    @staticmethod
    def parse_data_coal_dust(mine_id):
        present_date = datetime.datetime.now()
        timestamp = datetime.datetime.timestamp(present_date)
        data = {
            "timestamp": timestamp,
            "measurementType": "COAL_DUST",
            "mineId": mine_id,
            "thresholdInfo": {
                "maxDustLevel": "4",
                "maxParticleSize": "4"
            }
        }
        return data


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'zone_type', 'mine')
    search_fields = ('name', 'description', 'zone_type__name', 'mine__name')
    list_filter = ('zone_type', 'mine')


@admin.register(ZoneType)
class ZoneTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
