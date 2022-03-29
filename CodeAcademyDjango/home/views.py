from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello from CodeAcademy')


def frog_news(request):
    return render(request, "home/frog.html")


def wolf_news(request):
    return render(request, "home/wolf.html")


def eagle_news(request):
    return render(request, "home/eagle.html")
