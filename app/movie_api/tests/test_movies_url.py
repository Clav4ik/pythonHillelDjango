import unittest
from django.test import Client
from django.urls import reverse

from main.models import Movie, Genre, Director, Actor

class PostMovieCaseTest(unittest.TestCase):
    # url = reverse('main:home')
    url = '/api/v1/movies'

    def setUp(self):
        self.client = Client()


    def test_get_movie_api(self):
        movie_all_data = self.client.get(self.url)
        self.assertEqual(movie_all_data.status_code, 200)

    def test_post_movie_api(self):
        response = self.client.post(self.url,
                                    data={'title': 'ff', 'release_date': '1111-11-11', 'genre': ['2'],
                                     'director': 10, 'actors': [2], 'data': 'qw'})
        self.assertEqual(response.status_code, 201)

    def tearDown(self):
        Movie.objects.filter(title='ff').delete()

