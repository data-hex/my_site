from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your views here.
def mainpage(request):
    response = render_to_string('blog/index.html')
    return HttpResponse(response)


def posts(request):
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