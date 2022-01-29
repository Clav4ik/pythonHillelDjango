from django.urls import path
from api_user_auth.views import LoginView, RegisterView, Logout
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('sign_up', cache_page(60)(RegisterView.as_view()), name = 'api_register'),
    path('sign_in', cache_page(60)(LoginView.as_view()), name = 'api_login'),
    path('logout', Logout.as_view(), name = 'api_logout'),
]