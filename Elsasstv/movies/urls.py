from django.contrib import admin
from django.urls import path

import movies.views as views

app_name = 'movies'

urlpatterns = [

    path('', views.home, name='home'),
    path('<int:movie_id>/detail', views.detail, name="detail"),
]