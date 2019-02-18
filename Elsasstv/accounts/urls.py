from django.contrib import admin
from django.urls import path
import accounts.views as views

app_name = 'accounts'

urlpatterns = [

    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('list_users', views.list_users, name='list_users'),
    path('<int:friend_id>/friend_request', views.friend_request, name='friend_request'),
    path('<int:friendship_id>/<int:status>/accept_or_refuse', views.accept_or_refuse, name='accept_or_refuse'),
    path('<int:friend_id>/delete_friend', views.delete_friend, name='delete_friend')
]