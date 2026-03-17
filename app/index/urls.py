from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cows/', views.cows, name='cows'),
    path('production/', views.production, name='production'),
    path('wholesale/', views.wholesale, name='wholesale'),
    path('forecasting/', views.forecasting, name='forecasting'),
    path('petroshop/', views.petroshop, name='petroshop'),
]