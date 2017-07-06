
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from pip._vendor import requests

from config import settings


def google_view(request):
    google_api_key = settings.GOOGLE_API_KEY
    fc_location = '37.5175531,127.0183731'
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
    url_params = {
        'location': '37.5175531, 127.0183731',
        'radius': '1000',
        'type': 'restaurant',
        'keyword': '햄버거',
        'key': google_api_key,
    }
    response = requests.get(url, params=url_params).json()
    print("응답결과 :", response)
    print(response['results'])
    context = {
        'google_api_key': google_api_key,
        'fc_location': fc_location,
        'response': response,
    }
    return render(request, 'google_view.html', context)

