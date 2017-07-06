from django.conf.urls import url

from . import views

appname = 'googleapp'
urlpatterns = [
    url(r'^$', views.google_view, name='google_view'),
]