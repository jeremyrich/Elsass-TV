from django.contrib import admin
from django.urls import path

import accounts.views as views

app_name = 'accounts'

urlpatterns = [

    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
]