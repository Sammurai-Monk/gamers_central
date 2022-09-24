from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from . import views



# Create your views here.
def profile_page(request):
    return render(request,'profile_page/profile_page.html',{'username':'Welcome Bruv'})


def home(request):
    return render(request, 'signup_template/base.html',)