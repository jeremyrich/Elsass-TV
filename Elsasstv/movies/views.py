from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from movies.models import Movie, Person
from movies.APIClient import APIClient
from accounts.get_friends import get_notif


def home(request):
    """View rendering the 100th more popular movies"""
    popular_movies = Movie.objects.order_by('-popularity')[:100]
    # Getting the requests for the notifications
    if request.user.is_authenticated:
        friend_requests = get_notif(request.user)
        nb_requests = len(friend_requests)
    return render(request, 'movies/home.html', locals())

def detail(request, movie_id):
    """View rendering the detailed informations of a movie""" 
    movie = get_object_or_404(Movie, pk=movie_id)
    person, director = APIClient().get_movie_credits(movie_id)
    similar_movies = APIClient().get_similar_movies(movie_id)
    # Getting the requests for the notifications
    if request.user.is_authenticated:
        friend_requests = get_notif(request.user)
        nb_requests = len(friend_requests)
    return render (request, 'movies/movie-detail.html', locals())

def person(request, person_id):
    """View rendering the detailed informations of a person""" 
    person = get_object_or_404(Person, pk=person_id)
    known_for_ids = APIClient().get_person_credits(person_id)
    known_for=[]
    try: 
        for id in known_for_ids:
            known_for.append(Movie.objects.get(pk=id))
    except:
        pass
    # Getting the requests for the notifications
    if request.user.is_authenticated:
        friend_requests = get_notif(request.user) 
        nb_requests = len(friend_requests)        
    return render(request, 'movies/person-detail.html', locals())

def create_favorite(request, movie_id):
    """Allows the user to add a favorite"""
    movie = Movie.objects.get(pk=movie_id)
    current_user = request.user
    movie.users.add(current_user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove_favorite(request, movie_id):
    """Allows the user to remove a favorite"""
    movie = Movie.objects.get(pk=movie_id)
    user = request.user 
    movie.users.remove(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))