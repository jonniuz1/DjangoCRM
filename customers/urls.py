from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='home'), 
	path('add_customer/', views.add_customer, name='add_customer'),
	path('customer/<int:pk>/', views.customer, name='customer'), 
	path('update-customer/<int:pk>/', views.update_customer, name='update_customer'), 
	path('delete-customer/<int:pk>/', views.DeleteView.as_view(), name='delete_customer'),
	path('signup/', views.signup, name='signup'), 
	path('login/', views.login_customer, name='login'), 
	path('logout/', views.logout_customer, name='logout'), 
]

