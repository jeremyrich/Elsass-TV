
from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static

from movies.APIClient import APIClient
from .documents import MovieDocument
from accounts.get_friends import get_notif


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
    
    # Getting the requests for the notifications
    if request.user.is_authenticated:
        friend_requests = get_notif(request.user) 
        nb_requests = len(friend_requests)

    return render(request, 'search/home.html', locals())
