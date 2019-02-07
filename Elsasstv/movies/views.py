from django.shortcuts import render


def home(request):

    return render(request, 'movies/home.html', locals())
