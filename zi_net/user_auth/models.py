from django.db import models
from django.contrib.auth.models import AbstractUser
from vehicles import models as VehicleModels

class ZiUser(AbstractUser):
    phone_number = models.CharField(max_length=13, blank=True)
    gender = models.BooleanField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=5)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return 'User - ' + self.username
    
    @property
    def is_broker(self):
        return getattr(self, 'broker_profile', False)
    
    @property
    def is_customer(self):
        return getattr(self, 'customer_profile', False)


class Customer(models.Model):
    account = models.OneToOneField(ZiUser, blank=True, null=True, related_name='customer_profile', on_delete=models.CASCADE)
    interested_cars = models.ManyToManyField('vehicles.Vehicle', through='VehicleInterest', related_name='customers_interesed')


class Broker(models.Model):
    account = models.OneToOneField(ZiUser, blank=True, null=True, related_name='broker_profile', on_delete=models.CASCADE)
    interest_cars = models.ManyToManyField('vehicles.Vehicle', through='VehicleInterest', related_name='brokers_interesed')


class VehicleInterest(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    broker = models.ForeignKey('Broker', on_delete=models.CASCADE)
    vehicle = models.ForeignKey(VehicleModels.Vehicle, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    active = models.BooleanField()
    completed = models.BooleanField(default=False)