from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.urls import include
from . import views
urlpatterns = [
    path('',views.profile_page, name = 'profile_page'),
    path("home/", views.home, name="home"),
]
