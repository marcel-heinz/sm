from django.shortcuts import render
from django.http import HttpResponse
from opencage.geocoder import OpenCageGeocode
import requests


# Create your views here.

def home_page(request):
    city = request.POST.get('city_text', '')
    if city == "":
        return render(request, 'home.html', {'new_city_text': city, 'coord': ''})
    else:
        coordinates = get_lat_lon(city)
        uv_index = get_uv_index(coordinates)
        rec = uv_recommendation(uv_index, city)
        return render(request, 'home.html', {'new_city_text': city,
                                             'coord': coordinates, 'uv': uv_index,
                                             'uv_rec': rec})


def get_lat_lon(city):
    key_geo = 'e62d613e79e245e491c4458e65af41c2'
    geocoder = OpenCageGeocode(key_geo)
    results = geocoder.geocode(city)
    lat = results[0]['geometry']['lat']
    lon = results[0]['geometry']['lng']
    coordinates = [lat, lon]
    return coordinates


def get_uv_index(coordinates):
    api_key_open_weather = "71edc44595a7207a19ec4a304337667d"
    lat = coordinates[0]
    lon = coordinates[1]
    url = f"http://api.openweathermap.org/data/2.5/uvi?lat={lat}&lon={lon}&appid={api_key_open_weather}"
    response = requests.get(url)
    uv = response.json()
    uv = uv["value"]
    return uv


def uv_recommendation(uv_index, query):
    txt = ''
    if uv_index <= 2:
        txt = "UV Index is low.\nNo protection required."

    if 2 < uv_index <= 5:
        txt = "UV Index is moderate.\nSome protection required."

    if 5 < uv_index <= 7:
        txt = "UV Index is high.\nProtection is essential."

    if 7 < uv_index <= 10:
        txt = "UV Index is very high.\nExtra protection is needed."

    if uv_index > 10:
        txt = "UV Index is extreme.\nStay inside."
    return txt
