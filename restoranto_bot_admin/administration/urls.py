from django.urls import path

from . import views


app_name = 'administration'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_restaurant/', views.add_restaurant, name='add_restaurant'),
    path('add_info/', views.add_info, name='add_info'),
    path('add_table/', views.add_table, name='add_table'),
    path('get_tables/', views.get_tables, name='get_tables')
]
