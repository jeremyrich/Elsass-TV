from django.shortcuts import render, redirect
from movies.models import Movie
# from github.forms import LoginForm


def home(request):

    popular_movies = Movie.objects.order_by('-popularity')[:100] 
    

    return render(request, 'home.html', locals())

