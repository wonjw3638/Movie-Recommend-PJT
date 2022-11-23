from django.shortcuts import render, redirect
from .models import Choice
from .forms import ChoiceForm
from movies.views import Movie
from random import sample

from django.http import JsonResponse

def index(request):
    return render(request, 'choices/index.html')

def trailer(request):
    return render(request, 'choices/trailer.html')
    
def result(request):
    return render(request, 'choices/result.html')
    
# Create your views here.
def start(request):
    
    
    return render(request, 'choices/start.html')


def choose(request, option):
    choice = Choice.objects.first()
    movies = Movie.objects.all()
    selected_idx = sample(range(99), option)
    for idx in selected_idx:
        if choice.option_movies.count() == option:
            break
        choice.option_movies.add(movies[idx])
    context = {
        'selected_movie': choice.option_movies.all(),
        'option': option,
    }
    return render(request, 'choices/choose.html', context)


def main(request, idx, prefer):
    choice = Choice.objects.first()
    movie = choice.option_movies.all()[idx]
    if prefer == 'like':
        choice.like_movies.add(movie)
    else:
        choice.dislike_movies.add(movie)
    if idx == 4:
        return render(request, 'choices/final.html')
    next_movie = choice.option_movies.all()[idx + 1]
    print(choice.like_movies.all())
    print(choice.dislike_movies.all())
    context = {
        'title': next_movie.title,
        'id': next_movie.id,
    }
    return JsonResponse(context)


def final(request):
    print("yes")
    return render(request, 'choices/final.html')