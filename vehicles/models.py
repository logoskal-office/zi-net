from django.db import models
import general_data
import general_data.selection_data

class Vehicle(models.Model):
    producer = models.ForeignKey(to='Producer', verbose_name='Producer/Manufacturer', on_delete=models.DO_NOTHING)
    model = models.CharField(max_length=40, verbose_name='Model')
    common_name = models.CharField(blank=True, null=True, max_length=50, verbose_name='Common Name')
    production_year = models.PositiveIntegerField(blank=True, null=True, verbose_name='Production Year') # - size llimit
    production_country = models.CharField(blank=True, null=True, max_length=10, verbose_name='Production Country', choices=general_data.selection_data.CountryList)
    price = models.PositiveIntegerField(null=True, verbose_name='Price') # - size llimit
    price_negotiability = models.BooleanField(null=True, verbose_name='Negotiable')
    existing_debt = models.IntegerField(blank=True, null=True, default=0, verbose_name='Existing-Debt') # -  size limit
    body_type = models.CharField(null=True, max_length=20, choices=general_data.selection_data.VehicleBodyTypeList, verbose_name='Body Type')
    color = models.CharField(null=True, max_length=20, choices = general_data.selection_data.VehicleBodyColorList, verbose_name='Color')
    seat_size = models.PositiveIntegerField(blank=True, null=True, verbose_name='Number Of Seats') # - size limit
    cylinder_number = models.SmallIntegerField(blank=True, null=True, verbose_name='Cylinder Number') # - size limit    
    mileage = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Mileage') # - size limit
    condition = models.CharField(blank=True, null=True, max_length=20, choices=general_data.selection_data.VehicleCondition, verbose_name='Condition')
    condition_check = models.BooleanField(blank=True, null=True, choices={True:'Fully Checked', False:'Not-Fully Checked'})
    transmission = models.CharField(null=True, max_length=20, choices={'AU':'Automatic', 'MN':'Manual', 'SM': 'Semi-Auto', 'NN':'Other'}, verbose_name='Transmission')
    fuel_type = models.CharField(null=True, max_length=20, choices=general_data.selection_data.VehicleFuelType, verbose_name='Fuel')
    plate_number = models.PositiveIntegerField(blank=True, null=True, verbose_name='Plate Number') # - size limit
    plate_ownership = models.PositiveIntegerField(blank=True, null=True, verbose_name='Type of Plate Number')
    plate_state = models.CharField(blank=True, null=True, max_length=20, choices={'AA': 'Addis Ababa', 'OR': 'Oromia', 'FD':'Federal', 'NN':'Other'}, verbose_name='State Of Issued Plated')
    features = models.ManyToManyField('Feature', blank=True, verbose_name='Features')
    description = models.TextField(null=True, blank=True, verbose_name='Description', max_length=2000)
    issues = models.TextField(blank=True, null=True, max_length=2000)
    frozen = models.BooleanField(default=False)
    images = models.ImageField(blank=True, upload_to=f'albums/temp/')

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'
    
    def __str__(self):
        return self.producer.name + " " + self.model + f" ({self.id})"
        
class FeatureType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='logos/feature-type-logos')

    class Meta:
        verbose_name = 'Feature Type'
        verbose_name_plural = 'Feature Types'

    def __str__(self):
        return 'Feature Type - ' + self.name

class Feature(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    type = models.ForeignKey(FeatureType, on_delete=models.DO_NOTHING)
    logo = models.ImageField(upload_to='logos/feature-logos')

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return 'Feature - ' + self.name

class Producer(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    logo = models.ImageField(upload_to='logos/vehicle-producers/')

    class Meta:
        verbose_name = 'Producer'
        verbose_name_plural = 'Producers'

    def __str__(self):
        return self.name
#Check if there's an api to get car model data

