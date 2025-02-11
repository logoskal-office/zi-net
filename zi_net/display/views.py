from django.shortcuts import render

def home(request):
    return render(request, "display/home-page.html")

def test(request):
    return render(request, 'display/display.html')

