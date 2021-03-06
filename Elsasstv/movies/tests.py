from django.test import TestCase, SimpleTestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse, resolve

from Elsasstv.forms import RegisterForm, UserForm
from .models import Movie, Person
from .views import detail, home, person
from accounts.models import UserCustom, Friendship

import re 


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
        self.user1 = User.objects.create_user(id='1',username='test1', first_name='test', last_name='test', email='test@test.com', password="Test123456")
        self.user2 = User.objects.create_user(id='2',username='test2', first_name='test', last_name='test', email='test@test.com', password="Test123456")
        self.user_custom_1 = UserCustom.objects.create(id=self.user1.id, user=self.user1)
        self.user_custom_2 = UserCustom.objects.create(id=self.user2.id, user=self.user2)
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_home_view(self):
        movie = self.matrix       
        response = self.client.get(reverse('movies:home'))        
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        movie = self.matrix       
        response = self.client.get(reverse('movies:detail', kwargs={'movie_id':603}))
        self.assertEqual(response.status_code, 200)

    def test_has_movie_title(self):
        movie = self.matrix       
        response = self.client.get(reverse('movies:detail', kwargs={'movie_id':603}))
        body = str(response.content)
        m = re.search(r'[M][a][t][r][i][x]', body)
        self.assertTrue(m)
        
    def test_login_logout(self):
        self.client.login(username='test1', password='Test123456')
        response = self.client.get(reverse('movies:home'))
        self.assertTrue('<div id="header-username">Hi, test1</div>' in str(response.content))
        self.client.logout()
        response = self.client.get(reverse('movies:home'))
        self.assertFalse('<div id="header-username">Hi, testuser</div>' in str(response.content))
    
    def test_add_favorite(self):
        self.client.login(username='test1', password='Test123456')
        response = self.client.get(reverse('movies:create_favorite', kwargs={'movie_id': 603}))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.user1.movie_set.get(id=603).id, 603)
    
    def test_remove_favorite(self):
        self.client.login(username='test1', password='Test123456')
        self.matrix.users.add(self.user1)
        response = self.client.get(reverse('movies:remove_favorite', kwargs={'movie_id': 603}))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(len(self.user1.movie_set.all()), 0)
        
        


