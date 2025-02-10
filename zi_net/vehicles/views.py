from django.shortcuts import render, get_object_or_404
from .models import Vehicle

def list_all(request):
    return render(request, 'vehicles/list-all-vehicles.html')

def detail_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'vehicles/detail-vehicle.html', {'vehicle': vehicle})