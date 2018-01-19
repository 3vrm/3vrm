from django.urls import path
from . import views


urlpatterns = [
	path('', views.base),
	path('homepage/', views.homepage, name='homepage'),
	path('services/', views.services, name='services'),
]