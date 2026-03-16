from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cows/', views.cows, name='cows'),
    path('production/', views.production, name='production'),
]