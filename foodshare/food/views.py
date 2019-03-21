from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db import transaction
from django.views.generic import CreateView, TemplateView
from .forms import SignUpForm
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

    