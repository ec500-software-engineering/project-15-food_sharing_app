from django.urls import path
from . import views

urlpatterns = [
	path('', views.Index.as_view(), name='index'),
	path('food/<int:pk>', views.food_detail, name='food_detail'),
	path('food/<int:pk>/edit/', views.edit_food, name='food_edit'),
	path('food/<int:pk>/delete/', views.delete_food.as_view(), name='food_delete'),
	path('food/<int:pk>/claim/', views.claim_food, name='claim_food'),
	path('food/add', views.add_food, name='add_food'),
	path('food/view', views.food_list, name='food_list'),
]