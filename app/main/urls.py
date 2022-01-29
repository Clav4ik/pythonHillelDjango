from django.urls import path, include

from app import settings
from main.views import index, AllMovies, get_about_movie, get_top_movies, get_top_movies_int_value, Vote
from django.views.decorators.cache import cache_page

urlpatterns = [

    path('', index, name='index'),
    path('movies', AllMovies.as_view(), name='home'),
    path('movies/<int:movie_pk>', get_about_movie, name='about_movie'),
    path('movies/top', get_top_movies, name='top_movies'),
    path('movies/top/<int:int_value>', get_top_movies_int_value,
         name='top_movies_int_value'),
    path('movies/<movie_pk>/rate', Vote.as_view(), name='vote')

    ]