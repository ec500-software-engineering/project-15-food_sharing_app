from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	name =models.CharField(max_length=265)
	is_restaurant = models.BooleanField('restaurant status', default=False)
	is_person = models.BooleanField('person status', default=False)
	
class Restaurant(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	amount_gold = models.IntegerField()
	food_available = models.BooleanField(default = False)
	phone = models.CharField(max_length=265)