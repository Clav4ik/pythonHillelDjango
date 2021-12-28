
from django.urls import path
from django.views.decorators.cache import cache_page
from user_auth.views import RegisterFormViewUser, LoginUser, logout_user

urlpatterns = [

    path('register', cache_page(60)(RegisterFormViewUser.as_view()), name='register'),
    path('login', cache_page(60)(LoginUser.as_view()), name='login'),
    path('logout', logout_user, name='logout')
    ]