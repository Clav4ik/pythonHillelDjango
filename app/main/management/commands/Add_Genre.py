from django.core.management import BaseCommand


from main.models import Genre


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-ge', '--adge', type=int, default=10)

    def handle(self, *args, **options):
        all_default_genre = ['Action', 'Adventure', 'Animated', 'Comedy', 'Drama', 'Fantasy', 'Historical', 'Horror', 'Musical', 'Romance', 'Science Fiction', 'Thriller', 'Western']


        self.stdout.write("Start add genre")
        for i in range(len(all_default_genre)):
            genre = Genre()
            genre.title = all_default_genre[i]
            genre.save()
        self.stdout.write("End add genre")