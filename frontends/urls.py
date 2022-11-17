from django.urls import path
from . import views


app_name = 'frontends'

urlpatterns = [
    path('', views.index, name='index'),
    path('choice/', views.choice, name='choice'),
    path('trailer/', views.trailer, name='trailer'),
    path('result/', views.result, name='result'),
]