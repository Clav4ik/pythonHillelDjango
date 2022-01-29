from django.urls import path
from django.views.decorators.cache import cache_page

from .api_views import AllMovieListAPIView, TopMovieListAPIView, TopVaMovieLiluestAPIView, AboutMovieAPIView, \
    VoteAPIView

urlpatterns = [
    path('movies', cache_page(60)(AllMovieListAPIView.as_view()), name = 'all_apimovie'),
    path('movies/top', cache_page(60)(TopMovieListAPIView.as_view()), name = 'top_apimovie'),
    path('movies/top/<int:int_value>', cache_page(60)(TopVaMovieLiluestAPIView.as_view()),
         name='top_movies_int_value'),
    path('movies/<int:movie_pk>', cache_page(60)(AboutMovieAPIView.as_view()),
         name='about_movie_api'),
    path('movies/<int:movie_pk>/rate', VoteAPIView.as_view(),
         name='vote_api'),


]