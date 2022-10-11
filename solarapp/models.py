from django.db import models
from django.utils import timezone

# Create your models here.
class Weather(models.Model):
    name = models.CharField(max_length=20)
    country_code = models.CharField(max_length=5)
    longitude = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    latitude = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    temp = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    feels_like = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    pressure = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    time_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class SolarPredict(models.Model):
    time = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)
    humidity = models.CharField(max_length=50)
    pressure = models.CharField(max_length=50)
    precipitation = models.CharField(max_length=50)
    snowfall = models.CharField(max_length=50)
    total_cloud_cover = models.CharField(max_length=50)
    cloud_cover_high = models.CharField(max_length=50)
    cloud_cover_mid = models.CharField(max_length=50)
    cloud_cover_low = models.CharField(max_length=50)
    shortwave_radiation = models.CharField(max_length=50)
    wind_speed_10 = models.CharField(max_length=50)
    wind_direction_10 = models.CharField(max_length=50)
    wind_speed_80 = models.CharField(max_length=50)
    wind_direction_80 = models.CharField(max_length=50)
    wind_gusts = models.CharField(max_length=50)
    sun_altitude = models.CharField(max_length=50)
    sun_zenith = models.CharField(max_length=50)
    sun_distance = models.CharField(max_length=50)
    sun_azimuth = models.CharField(max_length=50)

    def __str__(self):
        return self.time