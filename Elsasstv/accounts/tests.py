from django.test import TestCase, Client
from accounts.models import UserCustom, Friendship
from django.contrib.auth.models import User
from django.urls import reverse, resolve


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(id='1',username='test1', first_name='test', last_name='test', email='test@test.com', password="Test123456")
        self.user2 = User.objects.create_user(id='2',username='test2', first_name='test', last_name='test', email='test@test.com', password="Test123456")
        self.user_custom_1 = UserCustom.objects.create(id=self.user1.id, user=self.user1)
        self.user_custom_2 = UserCustom.objects.create(id=self.user2.id, user=self.user2)
    
    def test_friend_request(self):
        self.client.login(username='test1', password='Test123456')
        response = self.client.get(reverse('accounts:friend_request', kwargs={'friend_id':2}))
        friendship = Friendship.objects.get(source_user=self.user_custom_1, target_user=self.user_custom_2)
        self.assertEquals(friendship.status, 0)

    def test_friend_accept(self):
        self.client.login(username='test2', password='Test123456')
        friendship = Friendship.objects.create(id=1, source_user=self.user_custom_1, target_user=self.user_custom_2, status=0)
        response = self.client.get(reverse('accounts:accept_or_refuse', kwargs={'friendship_id':1, 'status':1}))
        friendship = Friendship.objects.get(source_user=self.user_custom_1, target_user=self.user_custom_2)
        self.assertEquals(friendship.status, 1)
    
    def test_friend_refuse(self):
        self.client.login(username='test2', password='Test123456')
        friendship = Friendship.objects.create(id=1, source_user=self.user_custom_1, target_user=self.user_custom_2, status=0)
        response = self.client.get(reverse('accounts:accept_or_refuse', kwargs={'friendship_id':1, 'status':2}))
        friendship = Friendship.objects.get(source_user=self.user_custom_1, target_user=self.user_custom_2)
        self.assertEquals(friendship.status, 2)
    
    def test_delete_friend(self):
        self.client.login(username='test2', password='Test123456')
        friendship1 = Friendship.objects.create(id=1, source_user=self.user_custom_1, target_user=self.user_custom_2, status=1)
        friendship2 = Friendship.objects.create(id=2, source_user=self.user_custom_2, target_user=self.user_custom_1, status=1)
        response = self.client.get(reverse('accounts:delete_friend', kwargs={'friend_id':1}))
        friendship1 = Friendship.objects.get(source_user=self.user_custom_1, target_user=self.user_custom_2)
        friendship2 = Friendship.objects.get(source_user=self.user_custom_2, target_user=self.user_custom_1)
        self.assertEquals(friendship1.status, 2)
        self.assertEquals(friendship2.status, 2)
    


