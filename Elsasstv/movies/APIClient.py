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

    def get_movie_details(self, movie_id):
        """to get all the details of a movie"""
        url = 'https://api.themoviedb.org/3/movie/' + str(movie_id)
        full_url = self.call('GET', url)
        
    def get_similar_movies(self, movie_id):
        """to get similar movies to the page we're on"""
        url = 'https://api.themoviedb.org/3/movie/' + str(movie_id) + '/similar'
        full_url = self.call('GET', url)

        movies = []
        for movie in full_url['results']:
            movie['poster_path'] = 'https://image.tmdb.org/t/p/w200' + str(movie['poster_path'])
            movies.append(movie)

        return movies


    def get_movie_credits(self, movie_id):
        """to get the actors playing in a movie """
        url = 'https://api.themoviedb.org/3/movie/' + str(movie_id) + '/credits'
        full_url = self.call('GET', url)

        #Getting the cast
        cast = []
        for actor in full_url['cast']:
            profile_path = str(actor['profile_path'])

            if profile_path == str(None):
                actor['profile_path'] = 'https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg'
            else:
                actor['profile_path'] = 'https://image.tmdb.org/t/p/w200' + profile_path

            cast.append(actor)
            
        #Getting the director
        director = full_url['crew'][0]

        return cast, director

        # cast = full_url['cast']

        # for index, actor in enumerable(cast):
        #     cast[index]['profile_path'] = 'https://image.tmdb.org/t/p/w200' + str(actor['profile_path'])