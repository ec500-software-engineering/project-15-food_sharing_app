from django.urls import path
from . import views

urlpatterns = [
	path('', views.Index.as_view(), name='index'),
	# path('food/<int:pk>', views.food_detail, name='food_detail'),
	# path('food/add', views.add_food, name='add_food'),
]