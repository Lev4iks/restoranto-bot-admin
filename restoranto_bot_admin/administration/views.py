from django.shortcuts import render
from . import models


def index(request):
    return render(request, 'administration/index.html')


def addinfo(request):
    restaurant_name = models.Restaurant.name
