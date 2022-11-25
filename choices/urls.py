from django.urls import path
from . import views


app_name = 'choices'
urlpatterns = [
    path('', views.index, name='index'),
    path('start/', views.start, name='start'),
    path('<int:opt>/', views.option, name='option'),
    path('trailer/', views.trailer, name='trailer'),
    path('<int:idx>/<str:prefer>/', views.select, name='select'),
    path('result/', views.result, name='result'),
]
