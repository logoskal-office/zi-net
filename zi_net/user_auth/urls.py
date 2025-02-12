from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', login_view, name='login-page'),
    path('logout/', logout_view, name='logout-page'),
    path('register/', register_view, name='register-page'),
]