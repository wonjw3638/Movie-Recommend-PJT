from django.shortcuts import render, redirect
from .models import Choice
from .forms import ChoiceForm
from movies.views import Movie
from random import sample

from django.http import JsonResponse

def index(request):
    return render(request, 'choices/index.html')

def start(request):
    return render(request, 'choices/start.html')

def option(request, opt):
    choices = Choice.objects.all()
    choices.delete()
    
    choice = Choice(option=opt)
    choice.save()
    movies = Movie.objects.all()
    selected_idx = sample(range(100), opt)
    for idx in selected_idx:
        if choice.option_movies.count() == opt:
            break
        choice.option_movies.add(movies[idx])
    context = {
        'result': 1
    }
    return JsonResponse(context)

def trailer(request):
    choice = Choice.objects.last()
    movies = choice.option_movies.all()
    print(choice)
    context = {
        'movies': movies,
        'choice': choice,
    }
    return render(request, 'choices/trailer.html', context)

def select(request, idx, prefer):
    choice = Choice.objects.last()
    movie = choice.option_movies.all()[idx]
    if prefer == 'like':
        choice.like_movies.add(movie)
    else:
        choice.dislike_movies.add(movie)
    if idx == 4:
        print("es")
        return JsonResponse({'result': True})
    next_movie = choice.option_movies.all()[idx + 1]
    # print(choice.like_movies.all())
    # print(choice.dislike_movies.all())
    context = {
        'idx': idx,
        'title': next_movie.title,
        'id': next_movie.id,
        'trailer': next_movie.trailer_url,
        'result': False
    }
    return JsonResponse(context)
    
def result(request):
    choice = Choice.objects.last()
    like_movies = choice.like_movies.all()
    favs = list()
    for movie in like_movies:
        for genre in movie.genres.all():
            print(genre.name)
            favs.append(genre.name)
    print(favs)
    context = {
        'like_movies': like_movies
    }
    return render(request, 'choices/result.html', context)


def detail(request):
    return render(request, 'choices/detail.html') 