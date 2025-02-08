from django.shortcuts import render

def list_all(request):
    return render(request, 'vehicles/list-all-vehicles.html')
