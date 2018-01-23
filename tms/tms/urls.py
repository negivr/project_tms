from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home')
]


urlpatterns += [
    path('people/', include('people.urls', namespace='people')),
]

