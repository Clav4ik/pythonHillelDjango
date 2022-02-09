from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.http import HttpResponse, request
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm


# Create your views here.

class RegisterFormViewUser(CreateView):
    form_class = RegisterUserForm
    success_url = "login"
    template_name = 'user_auth/register.html'

    def form_valid(self, form):
        form.save()
        # get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        email = self.request.POST['email']
        # authenticate user then login
        user = authenticate(username=username, email=email, password=password)
        if user:
            # LoginUserForm(self.request, user)
            return super(RegisterFormViewUser, self).form_valid(form)
        return redirect('register', mes="incorectly email")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user_auth/login.html'

    def form_valid(self, form):
        # get the username and password

        username = self.request.POST['username']
        password = self.request.POST['password']
        email = self.request.POST['email']

        # authenticate user then login
        user = authenticate(request, username=username, password=password)

        if user.email == email:
            LoginUserForm(self.request, user)
            return super(LoginUser, self).form_valid(form)

        return HttpResponse("error email<br><a href='login'>return to login</a>")

    def get_success_url(self):
        return reverse_lazy("home")


# or in settings.py as LOGIN_REDIRECT_URL = ''


def logout_user(request):
    logout(request)
    return redirect('login')
