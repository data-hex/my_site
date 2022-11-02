from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def mainpage(request):
    return HttpResponse("Главная страница")


def posts(request):
    return HttpResponse("Все посты блога")


def get_post(request, name_post):
    return HttpResponse(f'<h1>Информация о посте {name_post}</h1>')
