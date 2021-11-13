from django.core.management import BaseCommand
from faker import Faker
from random import randrange, randint

from main.models import Actor, Movie


class Command(BaseCommand):
    help = "create fake movies with actors"

    def add_arguments(self, parser):
        parser.add_argument('-c', '--cmo', type=int, default=10)

    def handle(self, *args, **options):

        genre_list = ["cartoon", "no cartoon"]
        self.stdout.write("Start create movies with actors")
        print(options['cmo'])
        for _ in range(options['cmo']):
            faker = Faker()
            movie = Movie()

            movie.title = faker.sentence(nb_words=3)
            movie.genre = faker.word(ext_word_list=genre_list)
            movie.raiting = randint(-10, 10)
            movie.release_date = faker.date()
            movie.save()

            for _ in range(randrange(1,4)):
                actor = Actor()
                actor.name = faker.name()
                actor.save()
                movie.actors.add(actor)

            self.stdout.write(f'new movie\t{movie} {movie.genre}'
                              f' {movie.raiting} {movie.release_date} {movie.actors}')
        self.stdout.write("End create movies with actors")