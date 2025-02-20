from django.shortcuts import render

def landing(request):
    return render(request, "display/landing.html")

def home(request):
    return render(request, "display/home-page.html")

def test(request):
    return render(request, 'display/display.html')

def contact_us(request):
    return render(request, 'display/contact-us.html')

def about_us(request):
    return render(request, 'display/about-us.html')
