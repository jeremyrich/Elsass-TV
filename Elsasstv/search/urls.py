from django.contrib import admin
from django.urls import path

import search.views as views

app_name = 'search'

urlpatterns = [

    path('', views.home, name='home'),
]