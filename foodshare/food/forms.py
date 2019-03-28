from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import User
# , Food

number_validator = RegexValidator(
	r'^\D?(\d{3})\D?\D?(\d{3})\D?(\d{4})$', 
	"Make sure to use a US phone number"
)

class SignUpForm(UserCreationForm):
	name = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				'placeholder':'Name of your Restaurant'
			}
		)
	)
	phone = forms.CharField(
		required = True,
		validators = [number_validator],
		max_length = 10
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
