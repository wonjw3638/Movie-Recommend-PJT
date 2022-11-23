from django.db import models
from movies.views import Movie

# Create your models here.
class Choice(models.Model):
    option = models.CharField(max_length=10)
    option_movies = models.ManyToManyField(Movie, related_name='option_choices')
    like_movies = models.ManyToManyField(Movie, related_name='like_choices')
    dislike_movies = models.ManyToManyField(Movie, related_name='dislike_choices')