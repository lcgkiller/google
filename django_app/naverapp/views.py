import json
from django.shortcuts import render
import requests

# Create your views here.
from config import settings


def index(request):

    return render(request, "naverapp/index.html")


def search(request):
    import urllib.request
    client_id = settings.SECRET_NAVER_ID
    client_secret = settings.SECRET_NAVER_SECRET_KEY
    q = request.GET.get('q')
    encText = urllib.parse.quote("{}".format(q))
    url = "https://openapi.naver.com/v1/map/geocode?query=" + encText  # json 결과
    request_naver = urllib.request.Request(url)
    request_naver.add_header("X-Naver-Client-Id", client_id)
    request_naver.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request_naver)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        result = json.loads(response_body.decode('utf-8'))
        context = {
            'result': result
        }
        return render(request, 'naverapp/search_result.html', context)
    # else:
    #     print("Error Code:" + rescode)

    return render(request, 'naverapp/search_result.html')