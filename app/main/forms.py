from django.forms import ModelForm, TextInput, Textarea, DateInput

from main.models import Movie


class MovieCreateForm(ModelForm):
    class Meta:
        model = Movie
        fields = {'title', 'data', 'release_date', 'genre', 'director', 'actors'}

        widgets = {'title': TextInput(attrs={'placeholder': 'movie title'}),
                   "data": Textarea(attrs={
                       'placeholder': 'about movie'}),
                   'genre': TextInput(attrs={'placeholder': 'film genre'}),
                   'director': TextInput(attrs={'placeholder': 'film director'}),
                   'release_date': DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'required': 'required'}),
                   'actors': TextInput(attrs={'placeholder': 'film actor'}),
                   }
