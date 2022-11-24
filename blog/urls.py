from django.urls import path
from . import views

urlpatterns = [
    path('<int:number_post>/', views.get_number_post),
    path('<str:name_post>/', views.get_post),

]