from django.db import models


class Mine(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    code = models.CharField(max_length=20, verbose_name='Código', null=True, blank=True)
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    manager = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, verbose_name='Encargado',
                                related_name='mines')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mina'
        verbose_name_plural = 'Minas'


class ZoneType(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    code = models.CharField(max_length=20, verbose_name='Código', null=True, blank=True)
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - ' + self.code

    class Meta:
        verbose_name = 'Tipo de zona'
        verbose_name_plural = 'Tipos de zona'


class Zone(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    code = models.CharField(max_length=20, verbose_name='Código', null=True, blank=True)
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    zone_type = models.ForeignKey(ZoneType, on_delete=models.SET_NULL, null=True, verbose_name='Tipo de zona')
    mine = models.ForeignKey(Mine, on_delete=models.SET_NULL, null=True, verbose_name='Mina')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - ' + self.code

    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'
