from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from django.shortcuts import get_object_or_404

from vehicles import models as vehicle_models
from user_auth import models as user_models

from .serializers import *

class VehicleListView(APIView):
    def get(self, request):
        vehicles = vehicle_models.Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)
    
class VehicleDetailView(APIView):
    def get(self, request, pk):
        vehicle = get_object_or_404(vehicle_models.Vehicle, pk=pk)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)
    
