
from django.urls import path

from user_auth.views import RegisterFormViewUser, LoginUser, logout_user

urlpatterns = [

    path('register', RegisterFormViewUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout')
    ]