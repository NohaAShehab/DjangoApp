from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('DataFlair Django Tutorial<html><body><h1> Hello World DataFlair Dango tutorials</body></html>')

