from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cows/', views.cows, name='cows'),
    path('production/', views.production, name='production'),
    path('mpesa/', views.mpesa, name='mpesa'),
    path('value/', views.value, name='value'),
    path('feedinputs/', views.feedinputs, name='feedinputs'),
]