from django.contrib import admin
from .models import *

class VehicleInterestTabularInline(admin.TabularInline):
    model = VehicleInterest
    extra = 0
    verbose_name = 'Vehicle Of Interest'
    verbose_name_plural = 'Vehicles Of Interest'

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    inlines = [VehicleInterestTabularInline]

class BrokerAdmin(admin.ModelAdmin):
    model = Broker
    inlines = [VehicleInterestTabularInline]

# admin.site.register(ZiUser)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Broker, BrokerAdmin)