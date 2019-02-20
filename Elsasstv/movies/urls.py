from django.contrib import admin
from django.urls import path

import movies.views as views

app_name = 'movies'

urlpatterns = [

    path('', views.home, name='home'),
    path('<int:movie_id>/detail', views.detail, name="detail"),
    path('<int:person_id>/person-detail', views.person, name="person"),
    path('<int:movie_id>/favorite', views.create_favorite, name='create_favorite'),
    #path('<int:movie_id>/favorite', views.remove_favorite, name='remove_favorite'),
    
]