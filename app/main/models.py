from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Actor(models.Model):
    name = models.CharField("Actor name", max_length=60)

    def __str__(self):
        return self.name


class Genre(models.Model):
    title = models.CharField("Genre title", max_length=30)

    def __str__(self):
        return self.title


class Director(models.Model):
    name = models.CharField("Director name", max_length=60)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField("Movie title", max_length=50, db_index=True)
    data = models.TextField("Movie data", default="")
    picture = models.ImageField("Movie picture", null=True)
    genre = models.ManyToManyField(Genre)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True)
    release_date = models.DateField("Movie release_date", null=True)
    raiting = models.IntegerField("Movie raiting", default=0, db_index=True)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return '{} ({})'.format(self.title, self.release_date)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_notified = models.BooleanField(default= False)

    #other fields here

    def __str__(self):
          return "%s's profile" % self.user