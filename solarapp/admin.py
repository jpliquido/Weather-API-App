from django.contrib import admin
from .models import Weather, SolarPredict

# Register your models here.
admin.site.register(Weather)
admin.site.register(SolarPredict)