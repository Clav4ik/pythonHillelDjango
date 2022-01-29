from django.urls import path
from api_user_auth.views import LoginView, RegisterView, Logout


urlpatterns = [
    path('sign_up', RegisterView.as_view(), name = 'api_register'),
    path('sign_in', LoginView.as_view(), name = 'api_login'),
    path('logout', Logout.as_view(), name = 'api_logout'),
]