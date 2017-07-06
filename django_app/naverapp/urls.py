from django.conf.urls import url

from . import views

app_name="naverapp"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^naver/$', views.naver_map, name="naver_map"),
    url(r'^search/$', views.search, name="search"),
]