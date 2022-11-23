from django.contrib import admin
from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.main, name='main'),

    path('choose/', views.choose, name='choose'),
]
