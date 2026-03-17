from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cows/', views.cows, name='cows'),
    path('production/', views.production, name='production'),
    path('mpesa/', views.mpesa, name='mpesa'),
    path('value/', views.value, name='value'),
    path('feedinputs/', views.feedinputs, name='feedinputs'),
    path('wholesale/', views.wholesale, name='wholesale'),
    path('forecasting/', views.forecasting, name='forecasting'),
    path('petroshop/', views.petroshop, name='petroshop'),
    path('value-addition/', views.value_addition, name='value_addition'),
    path('feed-inputs/', views.feed_inputs, name='feed_inputs'),
    path('mpesa-ledger/', views.mpesa_ledger, name='mpesa_ledger'),
]