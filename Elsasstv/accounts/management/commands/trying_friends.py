"""
Import json data from URL to Datababse
"""
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
import requests
import json
from accounts.models import *
from django.contrib.auth.models import User
from datetime import datetime
import time
import sys

class Command(BaseCommand):
    def handle(self):
        user1 = User.objects.get(username='user1')

        # user3 = User.objects.get(username='user3').usercustom
        # friendship = Friendship(source_user = user2, target_user = user3, status = 2)
        # friendship.save()         
       
        friends=[]
        for friendship in Friendship.objects.filter(Q(source_user_id=user1.usercustom.id)): 
            # friendships.append(friendship)
            friends.append(friendship.target_user)            
        for friendship in Friendship.objects.filter(Q(target_user_id=user1.usercustom.id)): 
            # friendships.append(friendship)
            friends.append(friendship.source_user)  
        for friend in friends:
            print(friend.user.username)

test = Command()
print(test.handle())

    


