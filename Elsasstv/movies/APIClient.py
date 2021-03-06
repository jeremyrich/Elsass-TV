from django.conf import settings 
from django.contrib.staticfiles.templatetags.staticfiles import static

import requests 


class APIClient:
    """ Gets data from the movie db """ 

    def __init__(self):
        self.api_key = settings.API_KEY
    
    def call(self, method, url, **kwargs):
        response = None 
        if method == 'GET':
            url += '?api_key=' + str(self.api_key)
            for key in kwargs: 
                url += '&' + key + '=' + str(kwargs[key])
            response = requests.get(url)
        return response.json()
        
    def get_similar_movies(self, movie_id):
        """ gets similar movies to the page we're on """
        url = 'https://api.themoviedb.org/3/movie/' + str(movie_id) + '/similar'
        full_url = self.call('GET', url)
        movies = []
        for movie in full_url['results']:
            movie['poster_path'] = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2/' + str(movie['poster_path'])
            movies.append(movie)
        return movies

    def get_movie_credits(self, movie_id):
        """ gets the actors playing in a movie """
        url = 'https://api.themoviedb.org/3/movie/' + str(movie_id) + '/credits'
        full_url = self.call('GET', url)
        #Gets the cast
        cast = []
        for actor in full_url['cast']:
            profile_path = str(actor['profile_path'])
            if profile_path == str(None):
                actor['profile_path'] = static('images/not_available.png')
            else:
                actor['profile_path'] = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2/' + profile_path
            cast.append(actor)
        #Gets the director
        director = full_url['crew'][0]
        return cast, director

    def get_person_credits(self, person_id):
        """ gets all the informations for the person ID we'll use """
        url = 'https://api.themoviedb.org/3/person/' + str(person_id) + '/movie_credits'
        full_url = self.call('GET', url)
        movie_ids = [movie_id['id'] for movie_id in full_url['cast']]
        return movie_ids
        