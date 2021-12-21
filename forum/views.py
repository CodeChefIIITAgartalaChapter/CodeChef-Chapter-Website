from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'forum/home.html')

def about(request):
    return render(request,'forum/aboutUs.html')

def ml(request):
    return render(request,'forum/ML.html')

def CP(request):
    return render(request,'forum/CP.html')

def appDev(request):
    return render(request,'forum/appDev.html')

def webDev(request):
    return render(request,'forum/webDev.html')