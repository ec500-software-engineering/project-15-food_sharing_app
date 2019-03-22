from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class RestaurantProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	name = models.CharField(max_length=265)
	amount_gold = models.IntegerField(null=True, blank=True)
	food_available = models.BooleanField(default=False)
	phone = models.CharField(max_length=265)
	location = models.CharField(max_length=265, blank=True)

# class Food(models.Model):
# 	provider = models.ForeignKey(User, on_delete=models.CASCADE)
# 	title = models.CharField(max_length=255)
#	description = models.CharField(max_length=255)
# 	vegan = models.BooleanField(default=False)
# 	vegetarian = models.BooleanField(default=False)
# 	gluten_free = models.BooleanField(default=False)
# 	kosher = models.BooleanField(default=False)
# 	halal = models.BooleanField(default=False)