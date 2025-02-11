from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', login, name='login-page'),
    path('logout/', logout, name='logout-page'),
    path('register/', register, name='register-page'),
]