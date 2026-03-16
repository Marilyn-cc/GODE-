from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index/dashboard.html')

    
def cows(request):
    return render(request, 'index/cows.html')

def production(request):
    return render(request, 'index/production.html') 