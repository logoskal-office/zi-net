from django.contrib import admin
from .models import *

class VehicleImageTabularInline(admin.TabularInline):
    model = VehicleImage
    extra = 1

class VehicleAdmin(admin.ModelAdmin):
    inlines = [VehicleImageTabularInline]

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleImage)
admin.site.register(Producer)
admin.site.register(FeatureType)
admin.site.register(Feature)
