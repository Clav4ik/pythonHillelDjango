from django.core.management import BaseCommand
from faker import Faker


from main.models import Actor


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-fa', '--fact', type=int, default=10)

    def handle(self, *args, **options):
        actor = Actor()
        faker = Faker()
        self.stdout.write("Start create actors")
        for _ in range(options['fact']):
            actor = Actor()
            actor.name = faker.name()
            actor.save()
        self.stdout.write("End create actors")