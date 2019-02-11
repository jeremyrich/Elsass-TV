from django.test import TestCase
from django.urls import reverse

import re 

from .models import Movie
from .views import detail

class MovieTest(TestCase):

    def test_home_view(self):
        """Tests if the request to home page sends a response 200"""
        response = self.client.get(reverse('movies:home'))
        self.assertEqual(response.status_code, 200)

    def test_has_response(self):
        # testing if the page "detail" gives a correct http response
        movie = Movie.objects.create(id=1, title="Matrix")
        response = self.client.get(reverse('movies:detail', args=(movie.id,)))
        self.assertEqual(response.status_code, 200)

    def test_has_movie_title(self):
        # test if the page "detail" returns the right movie
        movie = Movie.objects.create(id=1, title="Matrix")
        response = self.client.get(reverse('movies:detail', args=(movie.id,)))
        body = str(response.content)
        m = re.search(r'[M][a][t][r][i][x]', body)
        self.assertEqual(m != None, True)
        
