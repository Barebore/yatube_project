from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    title = 'Yatube для авторов'
    context = {
        'title': title,
        'text': 'Это главная страница проекта Yatube',
    }
    return render(request, template, context) 

def group_posts(request):
    template = 'posts/group_list.html'
    title = 'Информация о группах проекта Yatube'
    context = {
        'title': title,
        'text': 'Здесь будет информация о группах проекта Yatube',
    }
    return render(request, template, context) 
