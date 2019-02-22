"""The module can be launched from the terminal using the command 'python3 manage.py import_movie'
""" 

from django.core.management.base import BaseCommand, CommandError

from movies.models import *
from datetime import datetime

import time
import json
import sys
import requests


class Command(BaseCommand):
    """Object from this class allows to fill the Movie model with movies from the dbmovie website"""

    def getIDs(self):
        """gets the ids of all movies, stored in a json file, and comparing them to ids of movies
        already in the database. Return the list of movies that are not yet in the database"""
        list_id = []
        with open('movie_ids_02_04_2019.json', 'r') as json_data:
            for line in json_data:
                data = json.loads(line)
                list_id.append(data['id'])
        # Getting the ids already present in the db
        In_db_movies = Movie.objects.all() 
        list_id_db = [film.id for film in In_db_movies]       
        # Removing the ids of the movies already in the db to avoid unecessary API calls
        list_id = list(set(list_id) - set(list_id_db)) 
        return list_id

    def handle(self, movie_id):
        """Makes a Get request to the movie db, knowing a movie_id"""
        response = requests.get(
            url='https://api.themoviedb.org/3/movie/'+ str(movie_id) + '?api_key=c7ee2bafbeec613e48d032777e99746f',
        )
        data = response.json()
        return self.createEntry(data)

    def createEntry(self, data):
        """Creates an entry in the database table corresponding to the Movie model"""
        try:
            movie, created = Movie.objects.get_or_create(
                id = data['id'],
                imdb_id = data["imdb_id"],
                original_title = data['original_title'],
                title = data['title'],
                tagline = data['tagline'],
                overview = data["overview"],
                release_date = data['release_date'],
                status = data['status'],
                runtime = data["runtime"],
                popularity = data['popularity'],
                original_language = data['original_language'],
                poster_path = data['poster_path'],
                backdrop_path =  data['backdrop_path'],
                budget = data['budget'],
                revenue = data['revenue'],
                vote_average = data['vote_average'],
                vote_count = data['vote_count'],
            )
            if created:
                movie.save()
        except Exception as ex:
            try:
                with open('errors_movies.txt', 'a') as errors:
                    errors.write(str(ex))
                    errors.write("\n\nSomething went wrong saving this movie: {}, id:{} \n{}".format(data['title'], data['id'], str(ex)))
            # In the case where either the fields 'title' or 'id' are empty, the movie is just not saved 
            except KeyError:
                pass

main = Command()
list_id = main.getIDs()

#Getting all the movies
for i in range(len(list_id)):
       main.handle(list_id[i])
   
    


