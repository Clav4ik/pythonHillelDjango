from rest_framework import filters
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, RetrieveUpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from main.models import Movie
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AllMovieSerializers, MovieRateSerializers


class AllMovieListAPIView(ListCreateAPIView):
    serializer_class = AllMovieSerializers
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['title', 'release_date']
    ordering_fields = ['title', 'release_date']
    ordering = ['-release_date']

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
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['title', 'release_date']
    ordering_fields = ['raiting']
    ordering = ['-raiting']
    queryset= Movie.objects.all()



class TopVaMovieLiluestAPIView(ListAPIView):
    serializer_class = AllMovieSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'release_date']

    def get_queryset(self):
        queryset = Movie.objects.order_by('-raiting')[:self.kwargs['int_value']]
        return queryset


class AboutMovieAPIView(ListAPIView):
    serializer_class = AllMovieSerializers

    def get_queryset(self):
        queryset = Movie.objects.filter(pk=self.kwargs['movie_pk'])
        return queryset


class VoteAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, movie_pk):
        queryset = Movie.objects.get(pk=movie_pk)
        serializers = MovieRateSerializers(queryset)
        return Response(serializers.data)

    def post(self, request, movie_pk):
        if request.data == 1 or request.data == -1:
            queryset = Movie.objects.get(pk=movie_pk)
            queryset.raiting += request.data
            queryset.save()
            return self.get(request, movie_pk)
        return self.get(request, movie_pk)
