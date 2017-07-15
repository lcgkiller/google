from django.conf.urls import url, include

from . import views

app_name = "member"

urlpatterns = [
    url(r'^$', views.login),
    url(r'^signup/$', views.signup, name="django_signup"),
    url(r'^signup-ok/$', views.signup_ok, name="signup_ok"),
]