from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView, CreateView

from main.forms import MovieCreateForm
from main.models import Movie, Director, Actor, Genre


def index(request):
    return HttpResponse("There is no text here<br><a href='movies'>next page</a>")


class AllMovies(TemplateView):
    template_name = 'main/index.html'

    def get(self, request):
        movies = Movie.objects.order_by('-id')
        paginator = Paginator(movies, 20)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        error = ''
        form = MovieCreateForm()
        context = {
            'form': form,
            'error': error,
            'page_obj': page_obj,
            'title': 'All movies'
        }
        return render(request, 'main/index.html', context)

    def post(self, request):
        try:
            dir = request.POST.get('director')
            director = Director.objects.create(name=dir)
            actor = Actor.objects.create(name=request.POST['actors'])
            actor.save()
            movie = Movie.objects.create(title=request.POST['title'],
                                         data=request.POST['data'],
                                         release_date=request.POST['release_date'],
                                         director=director)

            movie.save()
            movie.actors.add(actor)
            genre = Genre.objects.get(title=request.POST['genre'])
            movie.genre.add(genre)
            return redirect('home')  # переадресация на страничку home
        except:
            return self.get(request)


def get_about_movie(request, movie_pk):
    post_about_movie = get_object_or_404(Movie, pk=movie_pk)
    return render(request, 'main/about_movie.html', {'title': post_about_movie,
                                                     "movie": post_about_movie})


def get_top_movies(request):
    movies = Movie.objects.order_by('-raiting')[:100]
    context = {'title': 'Top movies',
               "movies": movies}
    return render(request, 'main/top_movies.html', context)


def get_top_movies_int_value(request, int_value):
    movies = Movie.objects.order_by('-raiting')[:int_value]
    return render(request, 'main/top_movies.html', {'title': 'Top movies',
                                                    "movies": movies})


class Vote(TemplateView):
    template_name = 'user_auth/vote.html'

    def get(self, request, movie_pk):
        return render(request, 'main/vote.html')

    def post(self, request, movie_pk):
        movie = Movie.objects.get(pk=movie_pk)
        movie.raiting += int(request.POST['fav_language'])
        movie.save()
        return redirect('about_movie', movie_pk)
