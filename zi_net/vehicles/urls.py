from django.urls import path, include
from .views import *

urlpatterns = [
    path('all/', list_all),
    path('<int:pk>/', detail_vehicle),
    path('search/<str:key>/', search),
    ]