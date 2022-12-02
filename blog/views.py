from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
import random


posts = [
    {
        'title': 'Рыбалка',
        'description': 'Хорошо посидели',
        'date': '21 авг 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Commodi distinctio doloremque et fuga iste neque, pariatur quod sit veritatis voluptates?'
    },
    {
        'title': 'Париж',
        'description': 'Незабываемое путешествие',
        'date': '5 сент 2020',
        'content': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
                Commodi distinctio doloremque et fuga iste neque, pariatur quod sit veritatis voluptates?'''
    },
    {
        'title': 'Финал лиги чемпионов',
        'description': 'Реал опять выиграл ЛЧ',
        'date': '28 мая 2022',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Qui, rem.'
    },
    {
        'title': 'Охота на уток',
        'description': 'Ни одна утка не пострадала',
        'date': '7 дек 2019',
        'content': 'Lorem ipsum dolor sit amet.'
    },
    {
        'title': 'Фестиваль огурца',
        'description': 'Суздаль ждет тебя',
        'date': '12 июль 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci consectetur id inventore odit recusandae!'
    },
    {
        'title': 'Нашествие',
        'description': 'Даешь рок, но в следующем году',
        'date': '29 июль 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Est mollitia recusandae rem?'
    },
    {
        'title': 'Новый год',
        'description': 'Эх, еще один год пролетел',
        'date': '31 дек 2022',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. A architecto corporis fuga ipsam laboriosam, nesciunt non quae qui ut veniam.'
    },
]


# Create your views here.
def mainpage(request):
    random.shuffle(posts)
    context = {
        'posts': posts[0:3]
    }
    return render(request, 'blog/index.html', context=context)


def get_posts(request):
    return render(request, 'blog/list_detail.html')


def get_post(request, name_post: str):
    if "kianu" in name_post:
        data = {
            'year_born': 1967,
            'city_born': "Бейрут",
            'movie_name': "Матрица"
        }
        return render(request, f'blog/{name_post}.html', context=data)
    elif "guinnessworldrecords" in name_post:
        context = {
            'power_man': 'Narve Laeret',
            'bar_name': 'Bob’s BBQ & Grill',
            'count_needle': 1790,
        }
        return render(request, f'blog/{name_post}.html', context=context)
    data_post = {
        'name': name_post
    }
    return render(request, 'blog/detail_by_name.html', context=data_post)


def get_number_post(request, number_post: int):
    data_post = {
        'number': number_post
    }
    return render(request, 'blog/detail_by_number.html', context=data_post)