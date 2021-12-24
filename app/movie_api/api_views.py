from django.shortcuts import redirect
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, RetrieveUpdateAPIView, \
    get_object_or_404
from rest_framework.decorators import api_view, throttle_classes
from main.models import Movie
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from .serializers import AllMovieSerializers, MovieRateSerializers


class AllMovieListAPIView(ListCreateAPIView):
    serializer_class = AllMovieSerializers


    def get_queryset(self):
        queryset = Movie.objects.all()
        return queryset

    def post_queryset(self, serializer):
        try:
            serializer.save()
        except Exception as ex:
            print(ex)

class TopMovieListAPIView(ListAPIView):
    serializer_class = AllMovieSerializers
    queryset = Movie.objects.order_by('-raiting')[:100]

class TopVaMovieLiluestAPIView(ListAPIView):
    serializer_class = AllMovieSerializers
    def get_queryset(self):

        queryset = Movie.objects.order_by('-raiting')[:self.kwargs['int_value']]
        return queryset

class AboutMovieAPIView(ListAPIView):
    serializer_class = AllMovieSerializers

    def get_queryset(self):
        queryset = Movie.objects.filter(pk=self.kwargs['movie_pk'])
        return queryset

class VoteAPIView(APIView):


    def get(self, request, movie_pk):

        queryset = Movie.objects.get(pk=movie_pk)
        serializers = MovieRateSerializers(queryset)
        return Response(serializers.data)

    def post(self, request, movie_pk):

        if request.data==1 or request.data==-1:
            queryset = Movie.objects.get(pk=movie_pk)
            queryset.raiting += request.data
            queryset.save()
            return self.get(request, movie_pk)
        return self.get(request, movie_pk)