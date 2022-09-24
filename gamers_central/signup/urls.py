from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.urls import include
from . import views


urlpatterns = [
    path('', views.signup, name = 'signup'),
    path("login/", views.login_request, name="login"),
    path("home/", views.home, name="home"),
]
