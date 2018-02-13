from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'vehicles'


urlpatterns = [
    path('', views.VehicleListView.as_view(), name='all'),
    path('(?P<pk>\d+)/', views.VehicleDetailView.as_view(), name='detail'),
    path('create/', views.VehicleCreateView.as_view(), name='create'),
    path('update/(?P<pk>\d+)/', views.VehicleUpdateView.as_view(), name='update'),
    path('delete/(?P<pk>\d+)/', views.VehicleDeleteView.as_view(), name='delete'),
    # url(r'^search/$', views.search, name='search'),
    # url(r'^search/$', views.SearchFilterView.as_view(), name='search'),
]





