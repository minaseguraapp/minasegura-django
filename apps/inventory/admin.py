from django.contrib import admin

from .models import EquipmentType, Equipment, Maintenance


@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'equipment_type', 'mine', 'is_active')
    search_fields = ('name', 'description', 'equipment_type__name', 'mine__name')
    list_filter = ('equipment_type', 'mine', 'is_active')


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'description', 'execution_date')
    search_fields = ('equipment__name', 'description',)
    list_filter = ('execution_date', 'created_at')
