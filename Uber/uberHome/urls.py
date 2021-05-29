
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.home,name="Home"),
    path('Home',views.home,name="Home"),
    path('Register',views.Register,name="Register"),
    path('Login',views.Login,name="Login"),
    path('About',views.About,name="About"),
    path('Services',views.Services,name="Services"),
]