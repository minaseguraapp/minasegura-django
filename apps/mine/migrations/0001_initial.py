# Generated by Django 5.0 on 2024-01-30 00:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ZoneType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('code', models.CharField(max_length=20, verbose_name='Código')),
                ('description', models.CharField(max_length=250, verbose_name='Descripción')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tipo de zona',
                'verbose_name_plural': 'Tipos de zona',
            },
        ),
        migrations.CreateModel(
            name='Mine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='Código')),
                ('description', models.CharField(max_length=250, verbose_name='Descripción')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Encargado')),
            ],
            options={
                'verbose_name': 'Mina',
                'verbose_name_plural': 'Minas',
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('code', models.CharField(max_length=20, verbose_name='Código')),
                ('description', models.CharField(max_length=250, verbose_name='Descripción')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mine.mine', verbose_name='Mina')),
                ('zone_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mine.zonetype', verbose_name='Tipo de zona')),
            ],
            options={
                'verbose_name': 'Zona',
                'verbose_name_plural': 'Zonas',
            },
        ),
    ]