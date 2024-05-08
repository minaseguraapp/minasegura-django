from django.db import models

from apps.mine.models import Mine


class EquipmentType(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de equipo'
        verbose_name_plural = 'Tipos de equipo'


class Equipment(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.SET_NULL, null=True,
                                       verbose_name='Tipo de equipo')
    mine = models.ForeignKey(Mine, on_delete=models.SET_NULL, null=True, verbose_name='Mina')
    image = models.ImageField(upload_to='equipment', null=True, blank=True, verbose_name='Imagen')
    is_active = models.BooleanField(default=True, verbose_name='¿Activo?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'


class Maintenance(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True, verbose_name='Equipo')
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    execution_date = models.DateTimeField(verbose_name='Fecha de realización', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return f'{self.equipment}'

    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'
