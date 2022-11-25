from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.http import JsonResponse

from collections import defaultdict
from movies.models import Movie, Genre
from django.db.models.query import QuerySet

from .forms import CustomUserCreationForm, CustomAuthenticationForm


# 회원가입
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('choices:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            form.save()
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('choices:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


# 로그인
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('choices:index')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'choices:index')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


# 로그아웃
@require_POST
def logout(request):
    auth_logout(request)
    return redirect('choices:index')


# 프로필 페이지
@login_required
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    choices = person.choice_set.all()

    # 유저가 했던 테스트들에서 선택했던 영화의 모든 장르를 추합하고 상위 3개를 골라낸다
    genre_list = defaultdict(int)
    like_list = []
    for choice in choices:
        for like_movie in choice.like_movies.all():
            like_list.append(like_movie)
            for genre in like_movie.genres.all():
                genre_list[genre.id] += 1
    top_genres = list(dict(sorted(genre_list.items(), key=lambda x:-x[1])).keys())[:3]

    # 상위 3개 장르의 이름 가져온다
    genre_names= []
    for genre in top_genres:
        genre_names.append(Genre.objects.get(pk=genre).name)
    context = {
        'person': person,
        'genre_names': genre_names
    }
    return render(request, 'accounts/profile.html', context)


# template에서 genre의 버튼을 누르면 해당 장르의 영화를 가져오는 기능을 하게 하려 했으나...
# 결국에는 그냥 선택했던 모든 영화들 / 장르 1, 2, 3의 영화들을 가져오는 기능을 하게 만듦
def genre(request, username, genre):
    person = get_object_or_404(get_user_model(), username=username)
    choices = person.choice_set.all()
    
    final = []
    genre_list = defaultdict(int)
    like_list = []
    # 선택했던 모든 영화들
    for choice in choices:
        for like_movie in choice.like_movies.all():
            movie = {
                'pk': int(like_movie.id),
                'title': like_movie.title,
                'poster': like_movie.poster_path
            }
            like_list.append(movie)
            # 해당 영화에 포함된 장르의 카운트를 += 1
            for genre_type in like_movie.genres.all():
                genre_list[genre_type.id] += 1
    final.append(like_list)
    # 상위 3개 장르
    top_genres = list(dict(sorted(genre_list.items(), key=lambda x:-x[1])).keys())[:3]

    # genre_names[0] = '모든'으로 설정하고 그 뒤에 각 장르의 영화 리스트를 추가했다
    genre_names = ['모든']
    for top_genre in top_genres:
        genre_names.append(Genre.objects.get(pk=top_genre).name)
        like_genres = list()
        for choice in choices:
            # print(choice.like_movies.all())
            for movie in choice.like_movies.filter(genres=top_genre):
                temp_movie = {
                    'pk': int(movie.id),
                    'title': movie.title,
                    'poster': movie.poster_path
                }
                like_genres.append(temp_movie)
        final.append(like_genres)
    context = {
        'genre_name': genre_names,
        'final': final,
    }
    return JsonResponse(context)

