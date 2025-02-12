from django.urls import path, include
from .views import *
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='list-vehicle-page')),
    path('all/', list_all, name='list-vehicle-page'),
    path('<int:pk>/', detail_vehicle, name='detail-vehicle-page'),
    path('search/<str:key>/', search, name = 'search-vehicle-page'),
    path('create/', create_vehicle, name = 'create-vehicle-page'),
    ]