from django.urls import path, include

from app import settings
from main.views import index, AllMovies, get_about_movie, get_top_movies, get_top_movies_int_value, Vote
from django.views.decorators.cache import cache_page

urlpatterns = [

    path('', cache_page(60)(index), name='index'),
    path('movies', cache_page(60)(AllMovies.as_view()), name='home'),
    path('movies/<int:movie_pk>', cache_page(60)(get_about_movie), name='about_movie'),
    path('movies/top', cache_page(60)(get_top_movies), name='top_movies'),
    path('movies/top/<int:int_value>', cache_page(60)(get_top_movies_int_value),
         name='top_movies_int_value'),
    path('movies/<movie_pk>/rate', cache_page(60)(Vote.as_view()), name='vote')

    ]