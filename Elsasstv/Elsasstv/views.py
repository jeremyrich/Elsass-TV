from django.shortcuts import render, redirect
from movies.models import Movie
from django.contrib.auth import login, authenticate, logout
from .forms import UserForm

def home(request):

    popular_movies = Movie.objects.order_by('-popularity')[:100] 

    # Beginning of login_user_form view
    error = False

    if request.method == 'POST':
        login_user = UserForm(request.POST)

        if login_user.is_valid():
            username = login_user.cleaned_data['username']
            password = login_user.cleaned_data['password']
            user = authenticate(username=username, password=password) 

            if user:  
                login(request, user)  
                return redirect('movies:home')
            else: 
                error = True                    

    else:
        login_user = UserForm() 
    # end of login_user_form view

    return render(request, 'home.html', locals())

