from django.shortcuts import render, HttpResponse


def login(request):
    return render(request, 'user_auth/login.html')

def logout(request):
    return render(request, 'user_auth/logout.html')

def register(request):
    return render(request, 'user_auth/register.html')