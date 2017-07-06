from django.conf.urls import url

from naverapp import views

urlpatterns = [
    url(r'^$/', views.index)
]