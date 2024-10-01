from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Articles
from .form import ArticleForm

# Create your views here.


def home_view(request):
    article_obj = Articles.objects.all()

    context = {
        'articles': article_obj
    }
    return render(request, 'home-view.html', context)


@login_required
def one_Article(request, id):

    article = Articles.objects.get(id=id)

    context = {
        'article': article
    }

    return render(request, 'articles.html', context)

@login_required
def article_create_view(request):
    article = Articles()
    form = ArticleForm(request.POST or None)
    # print(dir(form))

    if form.is_valid():
        article = form.save()
        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content')
        # article = Articles.objects.create(title=title, content=content)


    context = {
        'article': article,
        'created': True,
        'form': form
    }

    return render(request, 'create_article.html', context)

