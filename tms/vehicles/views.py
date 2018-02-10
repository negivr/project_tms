from django.shortcuts import render
# from .filters import VehicleFilter
# from django_filters.views import FilterView

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models


class VehicleListView(ListView):  # LoginRequiredMixin,
    context_object_name = 'vehicles'
    model = models.Vehicles


class VehicleDetailView(DetailView):  # LoginRequiredMixin,
    context_object_name = 'vehicle_detail'
    model = models.Vehicles
    template_name = 'vehicles/vehicle_detail.html'


class VehicleCreateView(CreateView):  # LoginRequiredMixin,
    fields = '__all__'
    model = models.Vehicles
    success_url = reverse_lazy('vehicles:all')
    template_name = 'vehicles/vehicle_form.html'


class VehicleUpdateView(UpdateView):  # LoginRequiredMixin,
    fields = '__all__'
    model = models.Vehicles
    template_name = 'vehicles/vehicle_form.html'


class VehicleDeleteView(DeleteView):
    model = models.Vehicles
    success_url = reverse_lazy('vehicles:all')
    template_name = 'vehicles/vehicle_confirm_delete.html'

