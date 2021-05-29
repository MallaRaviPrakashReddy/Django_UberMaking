
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')

def Register(request):
    if request.method=="POST":
        firstname=request.POST['firstName']
        lastname=request.POST['lastName']
        username=request.POST['userName']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirmPassword']
        if password==confirmpassword:
            if User.objects.filter(username=username):
                messages.info(request,"USername already exist")
                return render(request,'Register.html')
            elif User.objects.filter(email=email):
                messages.info(request,"email already exist")
                return render(request,'Register.html')
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,
                password=password)
                user.save()
                messages.info(request,'User Created')
                return render(request,'Login.html')
        else:
            messages.info(request,"Password didn't match")
            return render(request,'Register.html')
    else:
        print("not created")
        return render(request,'Register.html')

def Login(request):
    if request.method=="POST":
        Username=request.POST['userNameorEmail']
        Password=request.POST['password']
        user=auth.authenticate(username=Username,password=Password)
        if user is not None:
            auth.login(request,user)
            return render(request,'index.html') 
        else:
            messages.info(request,'User not recognized')
            return render(request,'Login.html')
    else:
        return render(request,'Login.html')
