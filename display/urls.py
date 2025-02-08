from django.contrib import admin
from django.urls import path, include
from display import views as display_views

urlpatterns = [
    path('', display_views.home, name='landing-page'),
    path('home/', display_views.home, name='home-page'),
]
