from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def mainpage(request):
    return HttpResponse("Главная страница")


def posts(request):
    return HttpResponse("Все посты блога")


def get_post(request, name_post: str):
    return HttpResponse(f'<h1>Информация о посте {name_post}</h1>')


def get_number_post(request, number_post: int):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')