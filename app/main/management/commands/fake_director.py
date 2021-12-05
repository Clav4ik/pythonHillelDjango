from django.core.management import BaseCommand
from faker import Faker

from main.models import Director


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-fd', '--fdir', type=int, default=10)

    def handle(self, *args, **options):

        faker = Faker()
        self.stdout.write("Start create directors")
        for _ in range(options['fdir']):
            director = Director()
            director.name = faker.name()
            director.save()
        self.stdout.write("End create directors")