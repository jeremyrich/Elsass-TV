from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from accounts.get_friends import get_notif, get_friends
from accounts.models import UserCustom, Friendship

from search.documents import UserDocument
from movies.models import Movie, Person


@login_required
def profile(request):
    """View rendering the details informations of a user"""
    current_user = request.user
    popular_movies = Movie.objects.order_by('-popularity')[:10]

    #Getting the friends
    friends = get_friends(current_user)
    nb_friends = len(friends)
    friend_ids = [friend.id for friend in friends]
    other_users = User.objects.exclude(Q(id=request.user.id) | Q(id=1)) 
    
    # Getting the requests for the notifications
    friend_requests = get_notif(request.user) 
    nb_requests = len(friend_requests)

    #search bar for username
    u = request.GET.get('u')
    if u:
        search = UserDocument.search().query("match", username=u)[:100]

    else:
        search = ''

    return render(request, 'accounts/profile.html', locals())

@login_required
def settings(request):
    """Displays all informations of the current user + modifications forms"""
    # Getting the requests for the notifications
    friend_requests = get_notif(request.user) 
    nb_requests = len(friend_requests)

    return render(request, 'accounts/settings.html', locals())

@login_required
def list_users(request):
    """Displays a list of all the current users, with the exception of the Elsasstv superuser, and the current user"""
    friends = get_friends(request.user)
    friend_ids = [friend.id for friend in friends]
    other_users = User.objects.exclude(Q(id=request.user.id) | Q(id=1)) 
    # Getting the requests for the notifications
    friend_requests = get_notif(request.user) 
    nb_requests = len(friend_requests)
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

@login_required
def accept_or_refuse(request, friendship_id, status):
    """Changing the status of the friendship between user. If the selected status is 1, the users are now friends,
    if its 2, the friendship is rejected
    """
    friendship = Friendship.objects.get(id=friendship_id)
    # Accepted
    if status == 1:
        friendship.status = 1
        friendship.save()
    # Refused
    else:
        friendship.status = 2
        friendship.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # Staying on the same page

@login_required
def delete_friend(request, friend_id):
    """Deletes a friend by looking for the corresponding relationship(s) and setting its status to 2"""
    friend = User.objects.get(id=friend_id)
    current_user = request.user 
    #Friendship where the current_user is the target   
    try:
        friendship1 = Friendship.objects.get(source_user=friend.usercustom, target_user=current_user.usercustom, status=1)
        if friendship1:
            friendship1.status = 2
            friendship1.save()
    except ObjectDoesNotExist:
        pass
    #Friendship where the current_user is the source
    try:
        friendship2 = Friendship.objects.get(source_user=current_user.usercustom, target_user=friend.usercustom, status=1)    
        if friendship2:
            friendship2.status = 2
            friendship2.save()
    except ObjectDoesNotExist:
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # Staying on the same page
    
@login_required
def friend_infos(request, friend_id):
    """Displays all the informations of a friend"""
    friend = User.objects.get(id=friend_id)
    popular_movies = Movie.objects.order_by('-popularity')[:10]
    # Getting the requests for the notifications
    friend_requests = get_notif(request.user) 
    nb_requests = len(friend_requests)
    return render(request, 'accounts/friend_infos.html', locals())     


