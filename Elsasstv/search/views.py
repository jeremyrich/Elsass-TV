
from django.shortcuts import render, get_object_or_404
from movies.models import Movie, Person
from movies.APIClient import APIClient
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.templatetags.staticfiles import static

from .documents import MovieDocument


# Create your views here.

def home(request):
    ''' This view will render all movies from a query (get from template form)'''

    # elasticsearch query
    q = request.GET.get('q')
    if q:
        search = MovieDocument.search().query("match", title=q)[:100]

        #replace None poster_path
        for i in search:
            if i['poster_path'] == None:
                i['poster_path'] = '/static/search/images/not_available.png'
            else:
                i['poster_path'] = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2/' + i['poster_path']
    else:
        search = ''

    return render(request, 'search/home.html', locals())
