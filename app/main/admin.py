from django.contrib import admin


from main.models import Movie, Genre, Director, Actor
# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Actor)
