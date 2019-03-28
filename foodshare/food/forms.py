from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
# , Food

class SignUpForm(UserCreationForm):
	name = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				'placeholder':'Name of your Restaurant'
			}
		)
	)
	phone = forms.IntegerField(
		widget = forms.NumberInput(
			attrs = {
				'placeholder':'Phone Number'
			}
		)
	)
	location = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				'placeholder':'Enter your address'
			}
		)
	)
	
	class Meta:
		model = User
		fields = ('name', 'phone', 'location', 'username','password1')

# class AddFoodForm(forms.ModelForm):
# 	class Meta:
# 		model = Food
# 		fields = ('title', 'description', 'vegan', 'vegetarian', 'gluten_free', 'kosher', 'halal')
