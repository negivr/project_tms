from django.contrib import admin
from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('', views.PeopleListView.as_view(), name='people_list'),
    path('fbv/', views.people_list_view, name='people_list_fbv'),
    path('<int:pk>/', views.PeopleDetailView.as_view(), name='detail'),
    path('fbv/<int:pk>/', views.people_detail_view, name='detail_fbv'),
]

