from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def register_view(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        user_obj = form.save()
        return redirect('/auth/login')

    context = {
        'form': form
    }
    return render(request, 'signup.html', context)

def logout_view(request):
    logout(request)
    return redirect('/auth/login')