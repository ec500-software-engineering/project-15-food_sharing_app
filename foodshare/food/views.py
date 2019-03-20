from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView
from .forms import RestaurantSignUpForm, PersonSignUpForm
from .models import User

# Create your views here.

class RestaurantSignUpView(TemplateView):
	model = User
	form_class = RestaurantSignUpForm
	template_name = 'registration/signup_form.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'restaurant'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('/')

class PersonSignUpView(TemplateView):
	model = User
	form_class = PersonSignUpForm
	template_name = 'registration/signup_form.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'person'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('/')

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

class Index(TemplateView):
	template_name = "food/index.html"

