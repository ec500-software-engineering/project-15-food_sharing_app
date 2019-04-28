from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from .forms import SignUpForm, AddFoodForm, ClaimFoodForm, EditProfile
from .models import User, RestaurantProfile, Food
import googlemaps

gmaps = googlemaps.Client('AIzaSyAilJRCrGRHf0AQJdkBBvbMYir7c3QvPfo')

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
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            phone = form.cleaned_data.get('phone')
            location = form.cleaned_data.get('location')
            user.save()
            profile = RestaurantProfile.objects.create(
                user_id = User.objects.get(username=user).id,
                name = name,
                phone = phone,
                location = location,
                email = email,
            )
            profile.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

    else:
        form = SignUpForm()

    context = {'form':form}
    return render(request, 'registration/signup.html', context)

@login_required
def add_food(request):
    if request.method == "POST":
        form = AddFoodForm(request.POST, request.FILES)
        restaurant = RestaurantProfile.objects.get(user=request.user)
        if form.is_valid():
            obj = Food(**form.cleaned_data)
            results = gmaps.geocode(restaurant.location)
            latitude = float('%.3f'%(results[0]['geometry']['location']['lat']))
            longitude = float('%.3f'%(results[0]['geometry']['location']['lng']))  
            obj.provider = restaurant.user
            obj.location = restaurant.location
            obj.lat = latitude
            obj.lng = longitude
            obj.save()
            return redirect('food_list')
        else :
            context = {'form': form}
            return render(request, 'food/add.html', context)
    else:
        form = AddFoodForm()
        context = {'form': form}
        return render(request, 'food/add.html', context)

@login_required
def edit_food(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == "POST":
        form = AddFoodForm(request.POST, instance=food)
        if form.is_valid():
            food = form.save(commit=False)
            food.provider = request.user
            food.save()
            return redirect('food_detail', pk=food.pk)
    else:
        form = AddFoodForm(instance=food)
    return render(request, 'food/food_edit.html', {'form': form})

class delete_food(LoginRequiredMixin, DeleteView):
    model = Food
    success_url = reverse_lazy('food_list')

def food_list(request):
    food = Food.objects.all()
    res = {'vegan': False, 'vegetarian': False, 'gluten_free': False}
    if request.method == "POST":
        restrictions = request.POST.getlist('restrictions')
        if 'vegan' in restrictions:
            food = food.filter(vegan=True)
            res['vegan'] = True
        if 'vegetarian' in restrictions:
            food = food.filter(vegetarian=True)
            res['vegetarian'] = True
        if 'gluten_free' in restrictions:
            food = food.filter(gluten_free=True)
            res['gluten_free'] = True
        food = food.filter(available=True)
        context = {'foods': food, 'restrictions': res}
        print(res)
        return render(request, 'food/food_list.html', context)
    else:
        food = food.filter(available=True)        
        print(res)
        context = {'foods': food, 'restrictions': res}
        return render(request, 'food/food_list.html', context)


def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    restaurant = RestaurantProfile.objects.get(user=food.provider) 
    context = {'food': food, 'restaurant': restaurant}
    return render(request, 'food/food_detail.html', context)

def claim_food(request, pk):
    if request.method == "POST":
        form = ClaimFoodForm(request.POST)
        food = Food.objects.get(pk=pk)
        restaurant = RestaurantProfile.objects.get(user=food.provider)  
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            food.available = False
            food.save()
            send_email(first_name, last_name, phone, email, restaurant, food)
            context = {'food': food, 'restaurant': restaurant}
            return render(request, 'food/claimed.html', context)
    else:
        form = ClaimFoodForm()
        context = {'form': form}
    return render(request, 'food/claim_food.html', context)


def send_email(first, last, phone, email, restaurant, food):
    connection = get_connection()
    # format email
    subject = "Food Claimed: " + food.title
    # email to restaurant
    res_message = "Hi {}, your food item: {}, has been claimed by {} {}. You can contact them at {} or by replying to this email.".format(restaurant.name, food.title, first, last, phone)
    res_email = EmailMessage(
        subject,
        res_message,
        settings.EMAIL_HOST_USER,
        [restaurant.email], 
        reply_to = [email,]
    )
    # email to claimer
    cus_message = "Hi {}, you claimed {} from {}. You can pick it up from {}. To contact the restaurant, call {} or reply to this email to email the restaurant directly.".format(first, food.title, restaurant.name, food.location, restaurant.phone)
    cus_email = EmailMessage(
        subject,
        cus_message,
        settings.EMAIL_HOST_USER,
        [email],
        reply_to = [restaurant.email,]
    )
    connection.send_messages([res_email, cus_email])

@login_required
def edit_profile(request):
    restaurant = RestaurantProfile.objects.get(user=request.user)
    if request.method == 'POST' :
       form = EditProfile(request.POST, instance=restaurant)
       if form.is_valid():
            form.save()
            return redirect('/food/view')

    else:
        form = EditProfile(instance=restaurant)
        context = {'form': form}
        return render(request, 'accounts/edit_profile.html', context)

@login_required
def foods_listed(request):
    food = Food.objects.all().filter(provider=request.user) 
    context = {'foods': food}
    return render(request, 'food/foods_listed.html', context)





