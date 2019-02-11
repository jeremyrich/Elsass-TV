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

# to get the actors playing in a movie 
    def get_movie_credits(self, movie_id):
        url = 'https://api.themoviedb.org/3/movie/' + str(movie_id) + '/credits'
        full_url = self.call('GET', url)
