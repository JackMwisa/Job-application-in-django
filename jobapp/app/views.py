from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def hello(request):
    return HttpResponse("Hello World")


def facilities(request):
    return HttpResponse("Our Hotel")