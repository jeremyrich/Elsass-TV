
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from movies.models import Movie, Person


@login_required
def profile(request):
    """View rendering the details informations of a user"""
    popular_movies = Movie.objects.order_by('-popularity')[:10]
    return render(request, 'accounts/profile.html', locals())

@login_required
def settings(request):

    return render(request, 'accounts/settings.html', locals())