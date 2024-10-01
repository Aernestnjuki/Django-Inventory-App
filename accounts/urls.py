from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='user-login'),
    path('signup/', views.register_view, name='user-register'),
    path('logout/', views.logout_view, name='logout-user')
]