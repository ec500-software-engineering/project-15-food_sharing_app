from django.contrib import admin
from .models import RestaurantProfile, Food

# Register your models here.
admin.site.register(RestaurantProfile)
admin.site.register(Food)