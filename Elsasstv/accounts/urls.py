from django.contrib import admin
from django.urls import path
import accounts.views as views

app_name = 'accounts'

urlpatterns = [

    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('list_users', views.list_users, name='list_users'),
    path('<int:friend_id>/friend_request', views.friend_request, name='friend_request')
]