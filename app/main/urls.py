from django.urls import path, include

from app import settings
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [

    path('', index, name='index'),
    path('home', home, name='home')
    ]