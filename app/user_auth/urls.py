




from django.urls import path, include

from app import settings
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [

    path('register', RegisterFormViewUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout')
    ]