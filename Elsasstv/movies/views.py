
from django.shortcuts import render, get_object_or_404
from movies.models import Movie, Person
from movies.APIClient import APIClient


def home(request):
    """View rendering the 100th more popular movies"""
    popular_movies = Movie.objects.order_by('-popularity')[:100]
    first_popular = Movie.objects.order_by('-popularity')[0]
    return render(request, 'movies/home.html', locals())

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    # person = Person.objects.filter(profile_path__isnull=False)[:3]
    person = APIClient().get_movie_credits(movie_id)
    # similar_movies = Movie.objects.order_by('-popularity')[:4]
    similar_movies = APIClient().get_similar_movies(movie_id)

    return render (request, 'movies/movie-detail.html', locals())

