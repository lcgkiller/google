from django.conf.urls import url

from . import views

app_name = "member"

urlpatterns = [
    url(r'^$', views.login, name="login"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^signup-ok/$', views.signup_ok, name="signup_ok"),
]