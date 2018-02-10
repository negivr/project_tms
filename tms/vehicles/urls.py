from django.conf.urls import url
from . import views


app_name = 'vehicles'


urlpatterns = [
    url('', views.VehicleListView.as_view(), name='all'),
    url('(?P<pk>\d+)/', views.VehicleDetailView.as_view(), name='detail'),
    url('create/', views.VehicleCreateView.as_view(), name='create'),
    url('update/(?P<pk>\d+)/', views.VehicleUpdateView.as_view(), name='update'),
    url('delete/(?P<pk>\d+)/', views.VehicleDeleteView.as_view(), name='delete'),
    # url(r'^search/$', views.search, name='search'),
    # url(r'^search/$', views.SearchFilterView.as_view(), name='search'),
]





