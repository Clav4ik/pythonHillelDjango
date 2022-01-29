from django.test import TestCase
import unittest
from django.test import Client
from django.urls import reverse

from main.models import Movie, Genre, Director, Actor



class PostMovieCaseTest(unittest.TestCase):
    # url = reverse('main:home')
    url = '/movies'

    def setUp(self):
        # pass
        self.client = Client()
        self.title = 'title movie'
        self.data = 'data movie'
        self.genre = Genre.objects.get(title='Action')
        self.director = Director.objects.get(name='Thomas Alexander')
        self.actors = Actor.objects.get(name='Amanda Jones')
        self.release_date = '1111-11-10'
        self.movie = Movie.objects.create(title=self.title,
                                          data=self.data,
                                          release_date=self.release_date,
                                          director=self.director)

        self.movie.save()
        self.movie.actors.add(self.actors)
        self.movie.genre.add(self.genre)

    def test_movie_create(self):
        self.assertIsInstance(self.movie, Movie)
        self.assertEqual(self.movie.title, "title movie")
        self.assertEqual(self.movie.director.name, 'Thomas Alexander')
        self.assertIsInstance(self.movie.genre.get(title='Action'), Genre)
        self.assertEqual(self.movie.actors.get(name='Amanda Jones').name, 'Amanda Jones')

    def test_get_movie(self):
        movie_all_data = self.client.get(self.url)
        self.assertEqual(movie_all_data.status_code, 200)

    def test_post_movie(self):
        csrf_client = Client(enforce_csrf_checks=True)
        response = self.client.post(self.url,
                                    data={'csrf': csrf_client, 'title': 'ff', 'release_date': '1111-11-11', 'genre': 'Drama',
                                     'director': 'Joe Villarreal', 'actors': 'Amanda Jones', 'data': 'qw'})
        self.assertEqual(response.status_code, 302)

    def tearDown(self):
        Movie.objects.filter(pk=self.movie.pk).delete()
        Movie.objects.filter(title='ff').delete()
        del self.movie
        del self.title
        del self.data
        del self.release_date
        del self.genre
        del self.director
        del self.actors

