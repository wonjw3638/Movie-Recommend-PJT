from django.shortcuts import render, redirect, get_object_or_404
from .models import Choice
from movies.models import Movie, Genre

from collections import defaultdict
from random import sample

from django.http import JsonResponse

def index(request):
    return render(request, 'choices/index.html')

def start(request):
    return render(request, 'choices/start.html')

def option(request, opt):
    choice = Choice(option=opt, user=request.user)
    choice.save()
    movies = list(Movie.objects.all())
    option_movies = sample(movies, opt)
    choice.option_movies.set(option_movies)
    # selected_idx = sample(range(100), opt)
    # for idx in selected_idx:
    #     if choice.option_movies.count() == opt:
    #         break
    #     choice.option_movies.add(movies[idx])
    context = {
        'result': opt
    }
    return JsonResponse(context)

def trailer(request):
    choice = Choice.objects.last()
    movies = choice.option_movies.all()
    context = {
        'movies': movies,
        'choice': choice,
    }
    return render(request, 'choices/trailer.html', context)

def select(request, idx, prefer):
    choice = Choice.objects.last()
    options = int(choice.option)
    movie = choice.option_movies.all()[idx]
    if prefer == 'like':
        choice.like_movies.add(movie)
    else:
        choice.dislike_movies.add(movie)
    if idx == options - 1:
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
    genre_list = defaultdict(int)
    for movie in like_movies:
        for genre in movie.genres.all():
            genre_list[genre.id] += 1
    like_genres = list(dict(sorted(genre_list.items(), key=lambda x:-x[1])).keys())[:3]
    genre_names = list()
    genre_recommends = dict()
    for like_genre in like_genres:
        genre_name = Genre.objects.get(pk=like_genre).name
        genre_movies = list(Movie.objects.filter(genres=like_genre))
        recommend = sample(genre_movies, 5)
        genre_names.append(genre_name)
        genre_recommends[genre_name] = recommend
        # print(genre_recommend)
    # print(like_genres)
    context = {
        'genre_names': genre_names,
        'genre_recommends': genre_recommends,
        'like_movies': like_movies
    }
    return render(request, 'choices/result.html', context)



# def detail(request, movie_pk):
def detail(request):
    movie = get_object_or_404(Movie, pk=10)
    comments = movie.comment_set.all()
    context = {
        'movie': movie,
        'comments': comments,
    }

    return render(request, 'choices/detail.html', context)