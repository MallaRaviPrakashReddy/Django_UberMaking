from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def Register(request):
    return render(request,'Accounts/Register')

def Login(request):
    return render(request,'Accounts/Login')

def About(request):
    return render(request,'About.html')

def Services(request):
    return render(request,'Services.html')