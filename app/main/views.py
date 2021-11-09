from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("There is no text here<br><a href='home'>next page</a>")

def home(request):
    return HttpResponse("Hello world!")