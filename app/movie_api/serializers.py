from rest_framework import serializers
from main.models import Movie

class AllMovieSerializers(serializers.ModelSerializer):
    # title = serializers.CharField(required = True)
    # data = serializers.CharField(required = True)
    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'data', 'genre', 'actors',
            'director', 'release_date', 'raiting'
        ]

class MovieRateSerializers (serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'raiting'
        ]