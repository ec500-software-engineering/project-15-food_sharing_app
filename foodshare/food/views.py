from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db import transaction
from django.views.generic import CreateView, TemplateView
from .forms import SignUpForm
# , AddFoodForm
from .models import User, RestaurantProfile

# Create your views here.
class Index(TemplateView):
	template_name = "food/index.html"

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            name = form.cleaned_data.get('name')
            phone = form.cleaned_data.get('phone')
            location = form.cleaned_data.get('location')
            user.save()
            profile = RestaurantProfile.objects.create(
                user_id = User.objects.get(username=user).id,
                name = name,
                phone = phone,
                location = location,
            )
            profile.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

    else:
        form = SignUpForm()

    context = {'form':form}
    return render(request, 'registration/signup.html', context)

# @login_required
# def add_food(request):
#     if request.method == "POST":
#         form = AddFoodForm(request.POST)
#         if form.is_valid():
#             food = form.save(commit=False)
#             provider = request.user
#             food.save()
#             available = RestaurantProfile.objects.get(user=request.user) #checks if user already has food availabe
#             if not availabe.food_available:
#                 availabe.food_available = True
#             availabe.save()
#             return redirect('/')
#     else:
#         form = AddFoodForm()
#         context = {'form': form}
#     return render(request, 'food/add_food.html', context)
    