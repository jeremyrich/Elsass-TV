from django.shortcuts import render, redirect
from movies.models import Movie
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, UserForm
from accounts.models import UserCustom, Friendship

def home(request):
    """View rendering the 100th more popular movies. Login and registration are managed from this
    view through a pop-up in the header"""

    # Request of the most popular movies
    popular_movies = Movie.objects.order_by('-popularity')[:100] 
    
    # Login    
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
        login_user = UserForm() 
        
    # Registration
    if request.method == 'POST':
        new_user = RegisterForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            new_username = new_user.cleaned_data.get('username')
            new_password = new_user.cleaned_data.get('password1')           
            user = authenticate(username=new_username, password=new_password)
            login(request, user)
            new_user_custom = UserCustom(id=user.id, user=user) # Creating a one to one linked custom user to create further friendships
            new_user_custom.save()
            return redirect('movies:home')
    else:
        new_user = RegisterForm()   
   
    return render(request, 'home.html', locals())

