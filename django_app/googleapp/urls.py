from django.conf.urls import url

from . import views

app_name = 'googleapp'
urlpatterns = [
    url(r'^$', views.google_view, name='google_view'),
]