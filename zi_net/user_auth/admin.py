from django.contrib import admin
from .models import *

class ZiUserAdmin(admin.ModelAdmin):
    model = ZiUser
    search_fields = ['username', 'id', 'first_name', 'last_name']

class VehicleInterestTabularInline(admin.TabularInline):
    model = VehicleInterest
    extra = 0
    verbose_name = 'Vehicle Of Interest'
    verbose_name_plural = 'Vehicles Of Interest'

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    inlines = [VehicleInterestTabularInline]
    search_fields = ['user__username', 'user__first_name', 'user__last_name',]
    autocomplete_fields = ['account']


class BrokerAdmin(admin.ModelAdmin):
    model = Broker
    inlines = [VehicleInterestTabularInline]
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    autocomplete_fields = ['account']

# admin.site.register(ZiUser)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Broker, BrokerAdmin)
admin.site.register(ZiUser, ZiUserAdmin)