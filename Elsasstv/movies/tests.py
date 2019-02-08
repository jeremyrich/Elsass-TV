from django.test import TestCase
from django.urls import reverse


class MovieTest(TestCase):

    def test_home_view(self):
        """Tests if the request to home page sends a response 200"""        
        response = self.client.get(reverse('movies:home'))
        self.assertEqual(response.status_code, 200)
