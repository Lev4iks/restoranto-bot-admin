from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from .models import Restaurant


def index(request):
    try:
        restaurant = Restaurant.objects.get(user_login=request.user)
        context = {'restaurant': restaurant}
    except ObjectDoesNotExist:
        context = {'restaurant': None}

    return render(request, 'administration/index.html', context)


def add_restaurant(request):
    return render(request, 'administration/add_restaurant.html')


def add_info(request):
    name = request.POST.get('name')
    address = request.POST.get('address')
    description = request.POST.get('description')
    Restaurant.objects.create(name=name, address=address, description=description, user_login=request.user)
    return redirect('administration:index')
