"""
Import json data from URL to Datababse
"""
from django.core.management.base import BaseCommand, CommandError
import requests
import json
from movies.models import *
from datetime import datetime
import time
import sys



class Command(BaseCommand):
    def createEntry(self, data):
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
                display_format = "\nMovie, {}, has been saved."
                print(display_format.format(movie))
        except Exception as ex:
            with open('errors_movies.txt', 'a') as errors:
                sys.stdout = errors
                print(str(ex))
                msg = "\n\nSomething went wrong saving this movie: {}, id:{} \n{}".format(data['title'], data['id'], str(ex))
                print(msg)
                sys.stdout = sys.__stdout__

    def getIDs(self):
        list_id = []
        with open('movie_ids_02_04_2019.json', 'r') as json_data:
            for line in json_data:
                data = json.loads(line)
                list_id.append(data['id'])

        return list_id

    def handle(self, movie_id):
        """
        Makes a GET request to the  API.
        """
        response = requests.get(
            url='https://api.themoviedb.org/3/movie/'+ str(movie_id) + '?api_key=c7ee2bafbeec613e48d032777e99746f',
        )
        data = response.json()

        return self.createEntry(data)

test  = Command()
list_id = test.getIDs()
for i in range(2500):
    test.handle(list_id[i])
    if i % 40 == 0 :
        time.sleep(1)
    


