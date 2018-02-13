from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('', views.PeopleListView.as_view(), name='all'),
    # path('fbv/', views.people_list_view, name='people_list_fbv'),
    path('<int:pk>/', views.PeopleDetailView.as_view(), name='detail'),
    # path('fbv/<int:pk>/', views.people_detail_view, name='detail_fbv'),
    path('create/', views.PeopleCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.PeopleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.PeopleDeleteView.as_view(), name='delete'),
]

