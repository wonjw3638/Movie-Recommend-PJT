from django.urls import path
from . import views


app_name = 'choices'
urlpatterns = [
    path('', views.index, name='index'),
    path('start/', views.start, name='start'),
    path('trailer/', views.trailer, name='trailer'),
    path('result/', views.result, name='result'),
    path('<int:option>/', views.choose, name='choose'),
    path('<int:idx>/<str:prefer>/', views.main, name='main'),
    path('final/', views.final, name='final'),
]
