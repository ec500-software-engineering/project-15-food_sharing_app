from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import User

class SignUpForm(UserCreationForm):
	name = forms.CharField(help_text='Enter the name of your restaurant')
	phone = forms.IntegerField(help_text='Enter your phone number')
	location = forms.CharField(help_text='Enter your address')
	
	class Meta:
		model = User
		fields = ('username','password1')
