from django.shortcuts import render
from movies.models import Movie


def home(request):
    """View rendering the 100th more popular movies"""
    popular_movies = Movie.objects.order_by('-popularity')[:100]    
    return render(request, 'movies/home.html', locals())
