from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Мой блог')


# Страница с публикациями друзей
def group_posts(request, slug):
    return HttpResponse(f'Публикации друзей {slug}')
