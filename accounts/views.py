from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                'error': 'Incorrect username or password'
            }
            return render(request, 'login.html', context)
        login(request, user)
        return redirect('/admin')
    context = {}
    return render(request, 'login.html', context)


def register_view(request):
    context = {}
    return render(request, 'login.html', context)

def logout_view(request):
    context = {}
    return render(request, 'login.html', context)