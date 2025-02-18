from django.urls import path
from .views import *

urlpatterns = [
    path('vehicles/all/', VehicleListView.as_view(), name='api-list-vehicles'),
    path('vehicles/<int:pk>/', VehicleDetailView.as_view(), name='api-detail-vehicle'),
]