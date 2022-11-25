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
    return HttpResponse(f'<h1>Информация о посте {name_post}</h1>')





def get_number_post(request, number_post: int):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')
