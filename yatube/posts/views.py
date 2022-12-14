from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Group, Post

def index(request):
    template = 'posts/index.html'
    title = 'Yatube для авторов'
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'text': title,
    }
    return render(request, template, context) 

def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Информация о группах проекта Yatube'
    # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'text': title,
    }
    return render(request, template, context) 
    return render(request, template, context) 
