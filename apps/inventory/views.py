from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from apps.inventory.forms import MaintenanceForm
from apps.inventory.models import Maintenance, Equipment


class MaintenanceListView(LoginRequiredMixin, ListView):
    template_name = "maintenance/list.html"
    model = Maintenance
    form = MaintenanceForm

    def get_queryset(self):
        return Maintenance.objects.filter(equipment__mine_id=self.kwargs.get('mine'))

    def get_form(self):
        form_queryset = Equipment.objects.filter(mine_id=self.kwargs.get('mine'))
        formset = self.form
        formset.base_fields['equipment'].queryset = form_queryset
        return formset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)
