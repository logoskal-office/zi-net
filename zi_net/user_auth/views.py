from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import ZiUserRegistrationForm

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/admin")  # Replace 'home' with the name of your desired redirect URL
        else:
            messages.error(request, "Invalid username or password")
            return HttpResponse(username, password)
    else:
        return render(request, 'user_auth/login.html')

def logout_view(request):
    return render(request, 'user_auth/logout.html')

def register_view(request):
    if request.method == 'POST':
        form = ZiUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # This saves the user and the profile (Customer/Broker)
            login(request, user)  # Log the user in after registration
            return redirect('create-profile-page')  # Redirect to a page after registration
    else:
        form = ZiUserRegistrationForm()

    return render(request, 'user_auth/register.html', {'form': form})

def create_profile(request):
    return None