from django.shortcuts import render, redirect
from movies.models import Movie
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, UserForm



def home(request):

    popular_movies = Movie.objects.order_by('-popularity')[:100] 


    #Registration
    if request.method == 'POST':
        new_user = RegisterForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            username = new_user.cleaned_data.get('username')
            raw_password = new_user.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('movies:home')
    else:
        new_user = RegisterForm()   

    # Login
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
   
    return render(request, 'home.html', locals())

