from django.contrib import admin
from .models import CarClass, CarUnit, Status, CarInstance

# Register your models here.
admin.site.register(CarUnit)
admin.site.register(CarClass)
admin.site.register(CarInstance)
admin.site.register(Status)
