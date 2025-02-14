from django.db import models
from django.contrib.auth.models import AbstractUser
from vehicles import models as VehicleModels
from general import validators

class ZiUser(AbstractUser):
    gender = models.BooleanField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    
    class Meta:
        verbose_name = 'User Account'
        verbose_name_plural = 'User Accounts'
    
    def __str__(self):
        _ = ''
        if self.first_name:
            _ += self.first_name.title() + ' '
        if self.last_name:
            _ += self.last_name.title()
        return 'User - ' + _ + f'(@{self.username} ID: {self.id})'
    
    @property
    def is_broker(self):
        return getattr(self, 'broker_profile', False)
    @property
    def is_customer(self):
        return getattr(self, 'customer_profile', False)


class Customer(models.Model):
    account = models.OneToOneField(ZiUser, blank=True, null=True, related_name='customer_profile', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, blank=True, validators=[validators.validate_ethiopian_phone_number])
    interested_cars = models.ManyToManyField('vehicles.Vehicle', through='VehicleInterest', related_name='customers_interesed')
    name = models.CharField(null=True, blank=True, default='', max_length=30)
    rating = models.PositiveSmallIntegerField(default=5)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        _ = ''
        if self.name:
            return self.name + f' (ID: {self.id})'
        elif self.account:
            if self.account.first_name:
                _ += self.account.first_name.title() + ' '
            if self.account.last_name:
                _ += self.account.last_name.title() + ' '
            return _ + f'(ID: {str(self.id)})'

class Broker(models.Model):
    account = models.OneToOneField(ZiUser, blank=True, null=True, related_name='broker_profile', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, blank=True, validators=[validators.validate_ethiopian_phone_number])
    interest_cars = models.ManyToManyField('vehicles.Vehicle', through='VehicleInterest', related_name='brokers_interesed')
    name = models.CharField(max_length=30, default='')
    rating = models.PositiveSmallIntegerField(null=True, blank=True, default=5)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.name:
            return self.name + f' (ID: {self.id})'
        elif self.account:
            if self.account.first_name:
                _ += self.account.first_name.title() + ' '
            if self.account.last_name:
                _ += self.account.last_name.title() + ' '
            return _ + f'(ID: {str(self.id)})'

class VehicleInterest(models.Model):
    customer = models.ForeignKey('Customer', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Interested Customer')
    broker = models.ForeignKey('Broker', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Through Broker')
    vehicle = models.ForeignKey(VehicleModels.Vehicle, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField()
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        _ = ''
        if self.customer:
            _ += 'Customer: ' + str(self.customer) + '  |  '
        if self.broker:
            _ += 'Broker: ' + str(self.broker) + '  |  '
        return _ + f'(Vehicle ID: ({self.id}))'