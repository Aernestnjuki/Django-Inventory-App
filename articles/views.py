from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles

# Create your views here.

def home_view(request):
    article_obj = Articles.objects.get(id=1)

    context = {
        'id': article_obj.id,
        'title': article_obj.title,
        'content': article_obj.content
    }


    return render(request, 'home-view.html', context)

