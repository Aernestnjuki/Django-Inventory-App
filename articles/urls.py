from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home-view'),
    path('articles/<int:id>', views.one_Article, name='article-by-id'),
    path('article/create/', views.article_create_view, name='create-article'),
]