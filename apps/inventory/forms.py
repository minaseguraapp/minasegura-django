from django import forms
from django.forms import ModelForm

from .models import Maintenance


class MaintenanceForm(ModelForm):
    class Meta:
        model = Maintenance
        fields = ['equipment', 'description', 'execution_date']
        labels = {
            'equipment': 'Equipo',
            'description': 'Descripción',
            'execution_date': 'Fecha de realización',
        }
        widgets = {
            'equipment': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'execution_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
        error_messages = {
            'equipment': {
                'required': 'Este campo es requerido',
            },
            'description': {
                'required': 'Este campo es requerido',
            },
            'execution_date': {
                'required': 'Este campo es requerido',
            },
        }
