from django.urls import path, include
from .views import *

urlpatterns = [
    path('', list_all),
    path('<int:pk>/', detail_vehicle)
    ]