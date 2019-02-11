import requests 
from django.conf import settings 

class APIClient: 

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

#to get all the details of a movie
    def get_movie_details(self, movie_id):
        url = 'https://api.themoviedb.org/3/movie/' + str(movie_id)
        full_url = self.call('GET', url)
        
    # to get similar movies to the page we're on
    def get_similar_movies(self, movie_id):
        url = 'https://api.themoviedb.org/3/movie/' + str(movie_id) + '/similar'
        full_url = self.call('GET', url)

        movies = []
        print(full_url)
        for movie in full_url['results']:
            movie['poster_path'] = 'https://image.tmdb.org/t/p/w200' + str(movie['poster_path'])
            movies.append(movie)

        return movies


    # to get the actors playing in a movie 
    def get_movie_credits(self, movie_id):
        url = 'https://api.themoviedb.org/3/movie/' + str(movie_id) + '/credits'
        full_url = self.call('GET', url)

        cast = []

        for actor in full_url['cast']:
            actor['profile_path'] = 'https://image.tmdb.org/t/p/w200' + str(actor['profile_path'])
            cast.append(actor)

        return cast

        # cast = full_url['cast']

        # for index, actor in enumerable(cast):
        #     cast[index]['profile_path'] = 'https://image.tmdb.org/t/p/w200' + str(actor['profile_path'])

        # return cast