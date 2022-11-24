from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Movie, Comment
from .forms import CommentForm
from django.http import JsonResponse

@require_GET
def detail(request, movie_pk):
# def detail(request):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comments = movie.comment_set.all()
    comment_form = CommentForm()
    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'movies/detail.html', context)

def get_comments(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comments = []
    for comment in movie.comment_set.all():
        print(comment.user.id)
        temp_comment = {
            'user_name': comment.user.username,
            'content': comment.content,
            'rating': comment.rating,
        }
        comments.append(temp_comment)
    context = {
        'comments': comments
    }
    return JsonResponse(context)


@require_POST
def create_comment(request, movie_pk):
    user_score = request.GET.get('user_score')
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment_form = CommentForm(request.POST)
    # user_score = int(request.GET['user_score'])
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.rating = user_score
        comment.save()
        return redirect('movies:detail', movie_pk)
