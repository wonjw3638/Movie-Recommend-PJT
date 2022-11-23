from django.shortcuts import render
import requests
from .models import Movie

# Create your views here.
def main(request):
    # API = '68172b7a51f513b96b7217ac3079c5df'
    # resDatas = []
    
    # for n in range(1, 6):
    #     num = str(n)
    #     LIST_URL = f"https://api.themoviedb.org/3/discover/movie?api_key={API}&language=ko-KR&page={num}"
    #     listData = requests.get(LIST_URL)
    #     resDatas.append(listData.json().get('results'))
    # context = {
    #     'resDatas': resDatas
    # }
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/main.html', context)


def choose(request):

    num = request.GET.get('option')
    print(num)
    return render(request, 'movies/choose.html')
    
