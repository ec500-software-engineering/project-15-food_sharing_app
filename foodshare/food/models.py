from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RestaurantProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	name = models.CharField(max_length=265)
	phone = models.CharField(max_length=265)
	location = models.CharField(max_length=265, blank=True)
	email = models.CharField(max_length=265, blank=True)

class Food(models.Model):
	provider = models.ForeignKey(User, on_delete=models.CASCADE)
	location = models.CharField(max_length=265)
	lat = models.FloatField(null=True)
	lng = models.FloatField(null=True)
	title = models.CharField(max_length=255)
	picture = models.ImageField(null=True, upload_to='images/')
	available = models.BooleanField(default=True)
	description = models.TextField()
	vegan = models.BooleanField(default=False)
	vegetarian = models.BooleanField(default=False)
	gluten_free = models.BooleanField(default=False)