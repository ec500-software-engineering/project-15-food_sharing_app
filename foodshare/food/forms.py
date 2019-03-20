from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Restaurant, User

class RestaurantSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ('name','phone number')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_resturant = True
        user.save()
        restaurant = Restaurant.objects.create(user=user)
        return user


class PersonSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_person = True
        if commit:
            user.save()
        return user
