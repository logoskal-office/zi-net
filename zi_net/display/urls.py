from django.contrib import admin
from django.urls import path, include
from display import views as display_views

urlpatterns = [
    path('', display_views.home, name='landing-page'),
    path('home/', display_views.home, name='home-page'),
    path('test/', display_views.test, name='test-page'),
    path('contact-us/', display_views.contact_us, name='contact-us-page'),
    path('about-us/', display_views.about_us, name='about-us-page'),
]
