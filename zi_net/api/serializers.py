from rest_framework import serializers

from vehicles import models as vehicle_models
from user_auth import models as user_models

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicle_models.Vehicle
        fields = (
            'owner',
            'broker',
            'producer',
            'model',
            'common_name',
            'production_year',
            'production_country',
            'price',
            'price_negotiability',
            'existing_debt', 
            'body_type', 
            'color', 
            'seat_size',
            'cylinder_number', 
            'mileage',
            'range',
            'battery_capacity',
            'condition', 
            'condition_check', 
            'transmission',
            'fuel_type', 
            'top_speed', 
            'horsepower',
            'zero_to_hundered', 
            'offroad',
            'plate_number', 
            'plate_ownership',
            'plate_state', 
            'features', 
            'description',
            'issues'
        )
class VehicleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicle_models.VehicleImage
        fields = ('vehicle', 'image')

class FeatureTypeSerializer(serializers.Serializer):
    class Meta:
        model = vehicle_models.FeatureType
        fields = ('name', 'description')

class FeatureSerializer(serializers.Serializer):
    class Meta:
        model = vehicle_models.Feature
        fields = ('name', 'description', 'type')

class ProducerSerializer(serializers.Serializer):
    class Meta:
        model = vehicle_models.Producer
        fields = ('name', 'description', 'logo')