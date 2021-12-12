from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
import requests
from django.views.decorators.csrf import csrf_exempt

from .models import Restaurant, Table


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


def add_table(request):
    name = request.POST.get('name')
    login = request.user

    try:
        Table.objects.create(login=login, name=name)
    except IntegrityError:
        return HttpResponse(500)
    return HttpResponse(200)


def get_tables(request):
    data = {
        "auth": "test",
        "name": request.user,
        "login": "test"
    }

    r = requests.post('http://91.122.61.223:3000/get_tables', data=data)
    print(r)
    return redirect('administration:index')

    # login = request.POST.get('login')
    # print(login)
    # tables = Table.objects.filter(login=login)
    # print(tables)
    # return HttpResponse(tables, content_type='application/json')
