from django.forms import ModelForm, Form, inlineformset_factory
from django.forms import models
import general_data
from .models import Vehicle, VehicleImage

class VehicleCreationForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'producer', 'model', 'common_name', 'production_year', 'production_country',
            'price', 'price_negotiability', 'existing_debt', 'body_type', 'color', 'seat_size',
            'cylinder_number', 'mileage','condition', 'condition_check', 'transmission',
            'fuel_type', 'top_speed', 'zero_to_hundered', 'plate_number', 'plate_ownership',
            'plate_state', 'features', 'description', 'issues'
        ]
        labels = {
            'issues': 'Are There Any Known Issues With The Car'
        }

class VehicleImageForm(ModelForm):
    class Meta:
        model = VehicleImage
        exclude = ['image']

VehicleImageInlineFormSet = inlineformset_factory(Vehicle, VehicleImage, form=VehicleImageForm, extra=1, fields=['image'])


class VehicleUpdateForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'producer', 'model', 'common_name', 'production_year', 'production_country',
            'price', 'price_negotiability', 'existing_debt', 'body_type', 'color', 'seat_size',
            'cylinder_number', 'mileage', 'condition', 'condition_check', 'transmission',
            'fuel_type', 'top_speed', 'zero_to_hundered', 'plate_number', 'plate_ownership',
            'plate_state', 'features', 'description', 'issues'
        ]
        labels = {
            'issues': 'Are There Any Known Issues With The Car'
        }
