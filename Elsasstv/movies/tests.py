from django.test import TestCase, SimpleTestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.http import HttpRequest  

import re 
import json
from Elsasstv.forms import RegisterForm, UserForm
from .models import Movie, Person
from .views import detail, home, person
from accounts.views import profile, settings
from movies.APIClient import APIClient



class TestMoviesUrls(SimpleTestCase):
    def test_home_url(self):
        url = reverse('movies:home')
        self.assertEquals(resolve(url).func, home)

    def test_detail_url(self):
        url = reverse('movies:detail', kwargs={'movie_id':1})
        self.assertEquals(resolve(url).func, detail)

    def test_person_url(self):
        url = reverse('movies:person', kwargs={'person_id':1})
        self.assertEquals(resolve(url).func, person)


class TestMoviesViews(TestCase):

    def setUp(self):
        self.client = Client()

        Movie.objects.create(id='603', original_title='test', title='test', tagline='test', overview='overview', status='test', original_language='test')
        Person.objects.create(id='135651', imdb_id='1', name='test', gender='1')

    def test_home_GET(self):
        response = self.client.get(reverse('movies:home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/home.html')

    def test_detail_GET(self):
        response = self.client.get(reverse('movies:detail',kwargs={'movie_id':603}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/movie-detail.html')

    def test_person_GET(self):
        response = self.client.get(reverse('movies:person',kwargs={'person_id':135651}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/person-detail.html')

class TestAccountUrls(SimpleTestCase):
    def test_profile_url(self):
        url = reverse('accounts:profile')
        self.assertEquals(resolve(url).func, profile)

    def test_settings_url(self):
        url = reverse('accounts:settings')
        self.assertEquals(resolve(url).func, settings)


class TestAccountViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', first_name='test', last_name='test', email='test@test.com', password="Test123456")

    def test_profile_GET(self):
        self.client.login(username='test', password='Test123456')
        response = self.client.get(reverse('accounts:profile'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile.html')

    def test_settings_GET(self):
        self.client.login(username='test', password='Test123456')
        response = self.client.get(reverse('accounts:settings'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/settings.html')


class Setup_Class(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', first_name='test', last_name='test', email='test@test.com', password="Test123456")

class TestForms(TestCase):


    def test_Registerform_Valid(self):

        form = RegisterForm(data={
            'username' : 'test', 
            'first_name' : 'test', 
            'last_name' : 'test', 
            'email' : 'test@test.com', 
            'password1' : 'Test123456', 
            'password2' : 'Test123456',
        })

        self.assertTrue(form.is_valid())


    def test_Registerform_invalid(self):

        form = RegisterForm(data={
            'username' : '', 
            'first_name' : '', 
            'last_name' : '', 
            'email' : '', 
            'password1' : '', 
            'password2' : '',
        })

        self.assertFalse(form.is_valid())

    def test_Loginform_valid(self):
        form = UserForm(data={
            'username' : 'test', 
            'password' : 'Test123456', })

        self.assertTrue(form.is_valid())

    def test_Loginform_invalid(self):
        form = UserForm(data={
            'username' : '', 
            'password' : '', })

        self.assertFalse(form.is_valid())

class MovieTest(TestCase):

    def setUp(self):       
        self.matrix = Movie.objects.create(id=603, title="Matrix")
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_home_view(self):
        """ Tests if the request to home page sends a response 200""" 
        movie = self.matrix       
        response = self.client.get(reverse('movies:home'))        
        self.assertEqual(response.status_code, 200)

    def test_has_response(self):
        """  testing if the page "detail" gives a correct http response""" 
        movie = self.matrix       
        response = self.client.get(reverse('movies:detail', kwargs={'movie_id':603}))
        self.assertEqual(response.status_code, 200)

    def test_has_movie_title(self):
        """ test if the page "detail" returns the right movie""" 
        movie = self.matrix       
        response = self.client.get(reverse('movies:detail', kwargs={'movie_id':603}))
        body = str(response.content)
        m = re.search(r'[M][a][t][r][i][x]', body)
        self.assertTrue(m)
        
    def test_login_logout(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('movies:home'))
        self.assertTrue('<div id="header-username">Hi, testuser</div>' in str(response.content))
        self.client.logout()
        response = self.client.get(reverse('movies:home'))
        self.assertFalse('<div id="header-username">Hi, testuser</div>' in str(response.content))
