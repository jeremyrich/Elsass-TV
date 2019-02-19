from accounts.models import UserCustom, Friendship
from django.db.models import Q

def get_friends(user):
	"""Function taking a user as argument and returning the list of his/her friends"""
	current_user = user
	friends=[]
	if user.username != 'Elsasstv':
		#Getting the target friendsf
		for friendship in Friendship.objects.filter(Q(source_user_id=current_user.usercustom.id) & Q(status=1)):
			friends.append(friendship.target_user.user)
		#Getting the source friends
		for friendship in Friendship.objects.filter(Q(target_user_id=current_user.usercustom.id) & Q(status=1)):
			friends.append(friendship.source_user.user)	
	return set(friends) # To avoid getting the same friend due to unsymmetrical friendships

def get_notif(user):
	"""Function taking a user as argument and returning the list of his/her in waiting friendships requests"""
	current_user = user
	friend_requests = []
	if current_user.username != 'Elsasstv':
		for friendship in Friendship.objects.filter(Q(target_user_id=current_user.usercustom.id) & Q(status=0)):
			friend_requests.append(friendship)
	return friend_requests