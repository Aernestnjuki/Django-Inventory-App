from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponse
from django.template.defaultfilters import title

from .models import Articles

# Create your views here.

def home_view(request):
    article_obj = Articles.objects.all()

    context = {
        'articles': article_obj
    }
    return render(request, 'home-view.html', context)

def one_Article(request, id):

    article = Articles.objects.get(id=id)

    context = {
        'article': article
    }

    return render(request, 'articles.html', context)


def article_create_view(request):
    print(request.POST)
    article = Articles()
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Articles.objects.create(title=title, content=content)

    context = {
        'article': article,
        'created': True
    }

    return render(request, 'create_article.html', context)

