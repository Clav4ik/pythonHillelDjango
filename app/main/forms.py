from datetime import date

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, CharField, PasswordInput, DateField, DateInput, Form
from django.shortcuts import redirect

from .models import Movie




class MovieCreateForm(ModelForm):
    class Meta:
        model = Movie
        fields = {'title', 'data', 'release_date','genre','director', 'actors' }

        widgets = {'title':TextInput(attrs={'placeholder': 'movie title'}),
                   "data": Textarea(attrs={
                       'placeholder': 'about movie'}),
                   'genre': TextInput(attrs={'placeholder': 'film genre'}),
                   'director': TextInput(attrs={'placeholder': 'film director'}),
                   'release_date': DateInput(attrs={'placeholder': 'YYYY-MM-DD','required': 'required'}),
                   'actors': TextInput(attrs={'placeholder': 'film actor'}),
                   }


