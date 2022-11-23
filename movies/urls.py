from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    # path('<int:review_pk>/', views.detail, name='detail'),
    # path('<int:review_pk>/comments/create/', views.create_comment, name='create_comment'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/comments/', views.get_comments, name='get_comments'),
    path('<int:movie_pk>/comments/create/', views.create_comment, name='create_comment'),
]
