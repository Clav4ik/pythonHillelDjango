from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField("Actor name", max_length=60)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField("Movie title", max_length=50)
    genre = models.CharField("Movie genre", max_length=30)
    release_date = models.DateField
    raiting = models.IntegerField("Movie raiting", default=0)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
            #'{} ({})'.format(self.title, self.release_date)
        return self.title