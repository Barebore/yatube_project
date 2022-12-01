from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def index(request):
    template = 'posts/index.html'
    title = 'Yatube для авторов'
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
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
