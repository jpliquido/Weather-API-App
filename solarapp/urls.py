from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('weather_updates/', views.weather_update, name='weather'),
    path('about/', views.about),
]