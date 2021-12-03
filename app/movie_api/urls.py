from django.urls import path

from .api_views import AllMovieListAPIView, TopMovieListAPIView, TopVaMovieLiluestAPIView, AboutMovieAPIView, \
    VoteAPIView

urlpatterns = [
    path('movies', AllMovieListAPIView.as_view(), name = 'all_apimovie'),
    path('movies/top', TopMovieListAPIView.as_view(), name = 'top_apimovie'),
    path('movies/top/<int:int_value>', TopVaMovieLiluestAPIView.as_view(),
         name='top_movies_int_value'),
    path('movies/<int:movie_pk>', AboutMovieAPIView.as_view(),
         name='about_movie_api'),
    path('movies/<int:movie_pk>/rate', VoteAPIView.as_view(),
         name='vote_api'),


]