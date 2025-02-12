from django.contrib import admin
from .models import *
from user_auth import models as user_models

class VehicleImageTabularInline(admin.TabularInline):
    model = VehicleImage
    extra = 0

class InterestedAccount(admin.TabularInline):
    model = user_models.VehicleInterest
    verbose_name = 'Interested Buyer'
    verbose_name_plural = 'Interested Buyers'
    extra = 0

class VehicleAdmin(admin.ModelAdmin):
    inlines = [VehicleImageTabularInline, InterestedAccount]
    search_fields = ['common_name', 'model', 'producer__name', 'id']
    autocomplete_fields = ['owner', 'broker']


admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleImage)
admin.site.register(Producer)
admin.site.register(FeatureType)
admin.site.register(Feature)
