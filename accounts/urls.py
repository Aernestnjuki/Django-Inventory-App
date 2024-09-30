from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='user-login'),
    path('signup/', views.login_view, name='user-register')
]