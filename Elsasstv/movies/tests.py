from django.test import TestCase
from django.urls import reverse

import re 

from .models import Movie
from .views import detail
from django.contrib.auth.models import User


class MovieTest(TestCase):

    def setUp(self):       
        self.matrix = Movie.objects.create(id=1, title="Matrix")
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_home_view(self):
        """Tests if the request to home page sends a response 200""" 
        movie = self.matrix       
        response = self.client.get(reverse('movies:home'))        
        self.assertEqual(response.status_code, 200)

    def test_has_response(self):
        """testing if the page "detail" gives a correct http response"""
        movie = self.matrix       
        response = self.client.get(reverse('movies:detail', args=(movie.id,)))
        self.assertEqual(response.status_code, 200)

    def test_has_movie_title(self):
        """test if the page "detail" returns the right movie"""
        movie = self.matrix       
        response = self.client.get(reverse('movies:detail', args=(movie.id,)))
        body = str(response.content)
        m = re.search(r'[M][a][t][r][i][x]', body)
        self.assertTrue(m)
        
    def test_login_logout(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('movies:home'))
        self.assertTrue('<div id="header-username">Hi, testuser</div>' in str(response.content))
        self.client.logout()
        response = self.client.get(reverse('movies:home'))
        self.assertTrue('<div id="header-username">Hi</div>' in str(response.content))

    
        
