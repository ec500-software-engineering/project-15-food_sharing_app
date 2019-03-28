from django.urls import path
from . import views

urlpatterns = [
	path('', views.Index.as_view(), name='index'),
	# path('food/<int:pk>', views.FoodDetail.as_view(), name='food_detail'),
	# path('food/add', views.add_food, name='add_food'),
	# path('food/view', views.food_list, name='food_list'),
]