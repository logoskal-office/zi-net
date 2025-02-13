# yourapp/middleware.py
from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define the list of paths to exempt from login check (login, logout, password reset, etc.)
        exempt_urls = [
            reverse('login-page'),  # Exempt the login page
            reverse('logout-page'),  # Exempt the logout page (if you have one)
            reverse('register-page')
        ]
        
        # Allow any URL that starts with '/auth/' or contains 'auth_user'
        if request.path.startswith('/auth/') or 'auth_user' in request.path:
            response = self.get_response(request)
        # If the user is not authenticated, and the URL is not exempt, redirect to login
        elif not request.user.is_authenticated and not any(request.path.startswith(url) for url in exempt_urls):
            return redirect(settings.LOGIN_URL)
        else:
            response = self.get_response(request)
        return response
