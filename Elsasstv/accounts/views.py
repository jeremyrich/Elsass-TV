
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User

from accounts.models import UserCustom, Friendship
from movies.models import Movie, Person


@login_required
def profile(request):
    """View rendering the details informations of a user"""
    popular_movies = Movie.objects.order_by('-popularity')[:10]
    current_user = request.user
    friends = []
    if current_user.username != 'Elsasstv':
        #Getting the target friends
        for friendship in Friendship.objects.filter(Q(source_user_id=current_user.usercustom.id) & Q(status=1)): 
            friends.append(friendship.target_user.user) 
        #Getting the source friends
        for friendship in Friendship.objects.filter(Q(target_user_id=current_user.usercustom.id) & Q(status=1)): 
            friends.append(friendship.source_user.user)
    nb_friends= len(friends)
            
    return render(request, 'accounts/profile.html', locals())


@login_required
def settings(request):

    return render(request, 'accounts/settings.html', locals())

@login_required
def list_users(request):
    """Displays a list of allt the current users, with the exception of the Elsasstv superuser, and the current user"""
    other_users = User.objects.exclude(Q(id=request.user.id) | Q(id=1)) 
    return render(request, 'accounts/list_users.html', locals())

@login_required
def friend_request(request, friend_id):
    """Sending a friend request to a user, and creating a new relationship"""
    current_user = request.user.usercustom
    target_user = User.objects.get(id=friend_id).usercustom
    new_friendship, created = Friendship.objects.get_or_create(source_user=current_user, target_user=target_user, status=0)
    if created:
        new_friendship.save()  
    return redirect('accounts:profile')
    

        


