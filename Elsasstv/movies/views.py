
from django.shortcuts import render, get_object_or_404
from movies.models import Movie


def home(request):
    """View rendering the 100th more popular movies"""
    popular_movies = Movie.objects.order_by('-popularity')[:100]    
    return render(request, 'movies/home.html', locals())

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render (request, 'movies/detail.html', {'movie' : movie})
