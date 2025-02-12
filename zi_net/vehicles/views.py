from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.db.models import Q
from .models import *
from .forms import *

def list_all(request):
    """
    # Create a producer instance
    producer = Producer.objects.create(
        name="Toyota",
        description="Japanese automaker known for reliability.",
        logo="logos/toyota_logo.jpg"
    )
    # Create a feature type
    feature_type = FeatureType.objects.create(
        name="Safety",
        description="Features related to safety",
    )

    # Create a feature instance
    feature = Feature.objects.create(
        name="Airbags",
        description="Standard airbags for safety",
        type=feature_type
    )

    # Create another feature
    feature2 = Feature.objects.create(
        name="Bluetooth",
        description="Wireless connectivity for mobile devices",
        type=feature_type
    )

    # Create a vehicle and associate the features
    vehicle = Vehicle.objects.create(
        producer=producer,
        model="Corolla",
        common_name="Corolla Sedan",
        production_year=2022,
        production_country="JP",  # assuming "JP" is a valid code in your selection_data.CountryList
        price=20000,
        price_negotiability=True,
        existing_debt=0,
        body_type="Sedan",  # assuming "Sedan" is in your general_data.selection_data.VehicleBodyTypeList
        color="Red",  # assuming "Red" is in your general_data.selection_data.VehicleBodyColorList
        seat_size=5,
        cylinder_number=4,
        mileage=0,
        condition="New",  # assuming "New" is in your general_data.selection_data.VehicleCondition
        condition_check=True,
        transmission="MN",  # assuming "MN" (Manual) is in your choices
        fuel_type="Gasoline",  # assuming "Gasoline" is in your general_data.selection_data.VehicleFuelType
        top_speed=180,
        zero_to_hundered=8.5,
        plate_number=123456,
        plate_ownership=1,
        plate_state="AA",  # assuming "AA" is in your plate_state choices
        description="Brand new Toyota Corolla Sedan.",
        issues="None",
        frozen=False,
    )

    # Add features to vehicle
    vehicle.features.add(feature, feature2)
    """

    context = {'vehicles':Vehicle.objects.all()}
    print(Vehicle.objects.all()[0].images.all())
    # print(Vehicle.objects.all()[1].images)
    # print(Vehicle.objects.all()[2].images)      
    # print(Vehicle.objects.all()[3].images)      
    return render(request, 'vehicles/list-all-vehicles.html', context)

def detail_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'vehicles/detail-vehicle.html', {'vehicle': vehicle})

def search(request, key: str):
    key = key.strip()
    filters = [' ', '#']
    if key in filters:
        pass
    else:
        results = Vehicle.objects.filter(
            Q(producer__name__icontains=key) | Q(model__icontains=key) | Q(common_name__icontains=key) | Q(description__icontains=key)
        )
        print(results)
        key = results
    return HttpResponse(key)

def create_vehicle(request):
    if request.method == 'POST':
        # Create forms for the Vehicle and the VehicleImage inline formset
        vehicle_form = VehicleCreationForm(request.POST)
        if vehicle_form.is_valid():
            vehicle = vehicle_form.save(commit=False)
            if request.user.is_customer:
                vehicle.owner = request.user.customer_profile
            if request.user.is_broker:
                vehicle.broker = request.user.broker_profile
            if 'images' in request.FILES:
                print('There are images')
                vehicle.save()
                images = request.FILES.getlist('images')
                print('Images :    ', images)
                for image in images:
                    VehicleImage.objects.create(vehicle=vehicle, image=image)

                return HttpResponse('Successful')
    else:
        return render(request, 'vehicles/create-vehicle.html', {'vehicle_creation_form':VehicleCreationForm})

def update_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        form = VehicleUpdateForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('detail-vehicle-page', pk=vehicle.pk)
    else:
        form = VehicleUpdateForm(instance=vehicle)
    
    return render(request, 'vehicles/update-vehicle.html', {'form': form})