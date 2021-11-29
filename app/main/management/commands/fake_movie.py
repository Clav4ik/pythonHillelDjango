from django.core.management import BaseCommand
from faker import Faker
from random import randrange, randint

from main.models import Actor, Movie, Genre, Director


class Command(BaseCommand):
    help = "create fake movies with actors, directors, genres existing in DB"

    def add_arguments(self, parser):
        parser.add_argument('-c', '--cmo', type=int, default=10)

    def handle(self, *args, **options):

        actors = Actor.objects.all()
        directors = Director.objects.all()
        genres = Genre.objects.all()
        self.stdout.write("Start create movies with actors and other objects")
        print(options['cmo'])
        for _ in range(options['cmo']):
            faker = Faker()
            movie = Movie()

            movie.title = faker.sentence(nb_words=3)
            movie.data = faker.text()

            movie.raiting = randint(-100, 100)
            movie.release_date = faker.date()
            movie.save()
            director = faker.word(ext_word_list=directors)
            director.movie_set.add(movie)
            for _ in range(randrange(1,5)):
                actor = faker.word(ext_word_list=actors)
                movie.actors.add(actor)
            for _ in range(randrange(1,3)):
                genre = faker.word(ext_word_list=genres)
                movie.genre.add(genre)

            self.stdout.write(f'new movie\t{movie} {movie.genre}'
                              f' {movie.raiting} {movie.release_date} {movie.actors}')
        self.stdout.write("End create movies with actors")