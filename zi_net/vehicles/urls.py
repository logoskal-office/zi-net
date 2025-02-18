from django.urls import path, include
from .views import *
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='list-vehicle-page')),
    path('search/', list_vehicles, name = 'list-vehicles-page'),
    path('all/', list_vehicles, name='list-all-vehicles-page'),
    path('<int:pk>/', detail_vehicle, name='detail-vehicle-page'),
    # path('search/<str:key>/', search_vehicle, name = 'search-vehicle-page'),
    path('create/', create_vehicle, name = 'create-vehicle-page'),
    path('edit/<int:pk>/', update_vehicle, name = 'update-vehicle-page'),
    ]