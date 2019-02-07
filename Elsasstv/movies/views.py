from django.shortcuts import render, get_object_or_404
from movies.models import Movie


def home(request):

    return render(request, 'movies/home.html', locals())

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render (request, 'movies/detail.html', {'movie' : movie})
