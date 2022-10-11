from django.shortcuts import render
import json
import urllib.request
from urllib import *
from urllib.parse import quote
from .models import Weather, SolarPredict
import ast
from math import sin, pi

# Create your views here.
def Home(request):
    if request.method == 'POST':
        city = request.POST['city']
        start_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=4f27b5f775d5d891c021ed183ce6e2bf"
        source = urllib.request.urlopen(start_url).read()
        list_of_data = json.loads(source)

        data = {
            "name":str(list_of_data['name']),
            "country_code":str(list_of_data['sys']['country']),
            "longitude":str(list_of_data['coord']['lon']),
            "latitude":str(list_of_data['coord']['lat']),
            "temp":str(list_of_data['main']['temp'] - 273.15),
            "feels_like":int(list_of_data['main']['feels_like'] - 273.15),
            "pressure":int(list_of_data['main']['pressure']),
            "humidity":int(list_of_data['main']['humidity']),
        }
        w = Weather(name=data['name'],
                    country_code=data['country_code'],
                    longitude=data['longitude'],
                    latitude=data['latitude'],
                    temp=data['temp'],
                    feels_like=data['feels_like'],
                    pressure=data['pressure'],
                    humidity=data['humidity']
                    )
        w.save()
        print(data)
    else:
        data = {}

    return render(request, 'solarapp/home.html', data)


def weather_update(request):
    if request.method == 'POST':
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']

        url1 = "https://api.open-meteo.com/v1/forecast?latitude="+latitude+"&longitude="+longitude+"&hourly=temperature_2m,relativehumidity_2m,pressure_msl,precipitation,snowfall,cloudcover,cloudcover_low,cloudcover_mid,cloudcover_high,shortwave_radiation,windspeed_10m,windspeed_80m,windspeed_120m,windspeed_180m,winddirection_10m,winddirection_80m,windgusts_10m"
        url2 = "https://api.ipgeolocation.io/astronomy?apiKey=ad559b5965d245eb95ce763b7e8c2d2f&lat="+latitude+"&long="+longitude
        source1 = urllib.request.urlopen(url1).read()
        source2 = urllib.request.urlopen(url2).read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source1)
        data = json.loads(source2)

        # data for variable list_of_data
        datalist = {
            "time":str(list_of_data['hourly']['time'][8:9]),
            "temperature_2m": str(list_of_data['hourly']['temperature_2m'][8:9]),
            "relativehumidity_2m": str(list_of_data['hourly']['relativehumidity_2m'][8:9]),
            "pressure_msl":str(list_of_data['hourly']['pressure_msl'][8:9]),
            "precipitation":str(list_of_data['hourly']['precipitation'][8:9]),
            "snowfall":str(list_of_data['hourly']['snowfall'][8:9]),
            "total_cloudcover":str(list_of_data['hourly']['cloudcover'][8:9]),
            "cloudcover_high":str(list_of_data['hourly']['cloudcover_high'][8:9]),
            "cloudcover_mid":str(list_of_data['hourly']['cloudcover_mid'][8:9]),
            "cloudcover_low":str(list_of_data['hourly']['cloudcover_low'][8:9]),
            "shortwave_radiation":str(list_of_data['hourly']['shortwave_radiation'][8:9]),
            "windspeed_10m":str(list_of_data['hourly']['windspeed_10m'][8:9]),
            "winddirection_10m":str(list_of_data['hourly']['winddirection_10m'][8:9]),
            "windspeed_80m":str(list_of_data['hourly']['windspeed_80m'][8:9]),
            "winddirection_80m":str(list_of_data['hourly']['winddirection_80m'][8:9]),
            "windgusts_10m":str(list_of_data['hourly']['windgusts_10m'][8:9]),
            "sun_altitude":str(data['sun_altitude']),
            "sun_zenith":str(90 - data['sun_altitude']),
            "sun_distance":str(data['sun_distance']),
            "sun_azimuth":str(data['sun_azimuth'])
        }

        solar = SolarPredict(
            time=datalist['time'],
            temperature=datalist['temperature_2m'],
            humidity=datalist['relativehumidity_2m'],
            pressure=datalist['pressure_msl'],
            precipitation=datalist['precipitation'],
            snowfall=datalist['snowfall'],
            total_cloud_cover=datalist['total_cloudcover'],
            cloud_cover_high=datalist['cloudcover_high'],
            cloud_cover_mid=datalist['cloudcover_mid'],
            cloud_cover_low=datalist['cloudcover_low'],
            shortwave_radiation=datalist['shortwave_radiation'],
            wind_speed_10=datalist['windspeed_10m'],
            wind_direction_10=datalist['winddirection_10m'],
            wind_speed_80=datalist['windspeed_80m'],
            wind_direction_80=datalist['winddirection_80m'],
            wind_gusts=datalist['windgusts_10m'],
            sun_altitude=datalist['sun_altitude'],
            sun_zenith=datalist['sun_zenith'],
            sun_distance=datalist['sun_distance'],
            sun_azimuth=datalist['sun_azimuth']
        )
        solar.save()

        print(type(datalist['time']))

        # ast.literak_eval() convert string to list
        def Convert(string):
            li = ast.literal_eval(string)
            return li
        
        print(type(Convert(datalist['time'])))
        
    else:
        datalist = {}
    
    return render(request, 'solarapp/weather_forecast.html', datalist)

"""
Solar Zenith angle is the angle between the sun's rays and the vertical direction.
Solar Altitude angle, which is the angle between the sun's rays and a horizontal plane
zenith angle = 90 - elevation
"""


def about(request):
    return render(request, 'solarapp/about.html')