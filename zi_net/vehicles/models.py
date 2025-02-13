from django.db import models
from user_auth import models as user_auth_models
from django.core.validators import MaxValueValidator, MinValueValidator
import general_data
import general_data.selection_data
import os
    
def get_upload_location_based_on_id(instance, filename):
    return os.path.join('vehicles', 'images', str(instance.id), filename)

class Vehicle(models.Model):
    owner = models.ForeignKey('user_auth.Customer', related_name='owned_cars', on_delete=models.DO_NOTHING, blank=True, null=True)
    broker = models.ForeignKey('user_auth.Broker', related_name='owned_cars', on_delete=models.DO_NOTHING, blank=True, null=True)
    producer = models.ForeignKey(to='Producer', verbose_name='Producer/Manufacturer', on_delete=models.DO_NOTHING)
    model = models.CharField(max_length=40, verbose_name='Model')
    common_name = models.CharField(blank=True, null=True, max_length=50, verbose_name='Common Name')
    production_year = models.PositiveIntegerField(blank=True, null=True, verbose_name='Production Year', validators=[MaxValueValidator(2025), MinValueValidator(1995)])
    production_country = models.CharField(blank=True, null=True, max_length=10, verbose_name='Production Country')
    price = models.PositiveIntegerField(null=True, verbose_name='Price') # - size llimit
    price_negotiability = models.BooleanField(null=True, verbose_name='Negotiable')
    existing_debt = models.IntegerField(blank=True, null=True, default=0, verbose_name='Existing-Debt') # -  size limit
    body_type = models.CharField(null=True, max_length=20, choices=general_data.selection_data.VehicleBodyTypeList, verbose_name='Body Type')
    color = models.CharField(null=True, max_length=20, choices = general_data.selection_data.VehicleBodyColorList, verbose_name='Color')
    seat_size = models.PositiveIntegerField(blank=True, null=True, verbose_name='Number Of Seats', validators=[MaxValueValidator(8), MinValueValidator(1)]) # - size limit
    cylinder_number = models.SmallIntegerField(blank=True, null=True, verbose_name='Cylinder Number', validators=[MaxValueValidator(16), MinValueValidator(3)]) # - size limit    
    mileage = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Mileage') # - size limit
    range = models.PositiveIntegerField(blank=True, null=True, verbose_name='Range In KM', validators=[MaxValueValidator(2000)])
    battery_capacity = models.PositiveIntegerField(blank=True, null=True, verbose_name='Battery Capacity In kWh', validators=[MaxValueValidator(500000)])
    condition = models.CharField(blank=True, null=True, max_length=20, choices=general_data.selection_data.VehicleCondition, verbose_name='Condition')
    condition_check = models.BooleanField(blank=True, null=True, choices={True:'Fully Checked', False:'Not-Fully Checked'})
    transmission = models.CharField(null=True, max_length=20, choices={'AU':'Automatic', 'MN':'Manual', 'SM': 'Semi-Auto', 'NN':'Other'}, verbose_name='Transmission')
    fuel_type = models.CharField(null=True, max_length=20, choices=general_data.selection_data.VehicleFuelType, verbose_name='Fuel')
    top_speed = models.PositiveIntegerField(blank=True, null=True, verbose_name="Top Speed")
    horsepower = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(2000)])
    zero_to_hundered = models.FloatField(blank=True, null=True, verbose_name='Accelaration (0 To 100)', validators=[MaxValueValidator(10), MinValueValidator(2)],)
    offroad = models.BooleanField(null=True, blank=True)
    plate_number = models.PositiveIntegerField(blank=True, null=True, verbose_name='Plate Number', validators=[MaxValueValidator(1), MinValueValidator(99999)]) # - size limit
    plate_ownership = models.CharField(blank=True, null=True, max_length=5, verbose_name='Type of Plate Number', )
    plate_state = models.CharField(blank=True, null=True, max_length=20, verbose_name='State Of Issued Plated')
    features = models.ManyToManyField('Feature', blank=True, verbose_name='Features')
    description = models.TextField(null=True, blank=True, verbose_name='Description', max_length=2000)
    issues = models.TextField(blank=True, null=True, max_length=2000)
    frozen = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'
    
    def __str__(self):
        return self.producer.name + " " + self.model + f" - {self.common_name} (ID: {self.id})"
        
class FeatureType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Feature Type'
        verbose_name_plural = 'Feature Types'

    def __str__(self):
        return 'Feature Type - ' + self.name

class Feature(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    type = models.ForeignKey(FeatureType, null=True, blank=True, on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return 'Feature - ' + self.name

class Producer(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    logo = models.ImageField(null=True, blank=True, default='default.jpeg', upload_to='logos/vehicle-producers/')

    class Meta:
        verbose_name = 'Producer'
        verbose_name_plural = 'Producers'

    def __str__(self):
        return self.name

class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='images', on_delete=models.CASCADE)
    image = models.FileField(upload_to='vehicles/images/')

    def __str__(self):
        return str(self.vehicle.producer.name + "'s Image - ") + str(self.vehicle.id)


#Check if there's an api to get car model data

