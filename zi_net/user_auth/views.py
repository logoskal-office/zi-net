from django.shortcuts import render, HttpResponse


def login(request):
    return HttpResponse(request, 'A')

def logout(request):
    return HttpResponse(request, 'A')

def register(request):
    return HttpResponse(request, 'A')