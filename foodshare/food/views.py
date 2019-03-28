from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# from django.db import transaction
from django.views.generic import TemplateView, ListView
from .forms import SignUpForm
# , AddFoodForm
from .models import User, RestaurantProfile
# , Food

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
#             obj = Food(**form.cleaned_data)
#             obj.provider = request.user
#             obj.save()
#             # title = form.cleaned_data.get('username')
#             # description = form.cleaned_data.get('password1')
#             # food_item = Food.objects.create(
#             #     provider = request.user,
#             #     title = food.title,
#             #     description = food.description,
#             #     vegan = food.vegan,
#             #     vegetarian = food.vegetarian,
#             #     gluten_free = food.gluten_free,
#             #     kosher = food.kosher,
#             #     halal = food.halal,
#             # )
#             # food_item.save()
#             # print("saved food")
#             available = RestaurantProfile.objects.get(user=request.user) #checks if user already has food availabe
#             if not availabe.food_available:
#                 availabe.food_available = True
#             availabe.save()
#             return redirect('food_list')
#     else:
#         form = AddFoodForm()
#         context = {'form': form}
#     return render(request, 'food/add.html', context)

# @login_required
# def food_edit(request, pk):
#     food = get_object_or_404(Food, pk=pk)
#     if request.method == "POST":
#         form = AddFoodForm(request.POST, instance=food)
#         if form.is_valid():
#             food = form.save(commit=False)
#             food.provider = request.user
#             food.save()
#             return redirect('food_list')
#     else:
#         form = AddFoodForm()
#     return render(request, 'food/food_edit.html', {'form': form})


# def food_list(request):
#     food = Food.objects.all()
#     context = {'foods': food}
#     return render(request, 'food/food_list.html', context)
#     # model = Food

#     