from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Users
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
  return render(request, "home/index.html")


def register(request):
  if request.method =="POST":
    form=RegisterForm(request.POST)
    if form.is_valid:
      username=form.cleaned_data["username"]
      password=form.cleaned_data["password1"]
      form.save()
      new_user=authenticate(
        username=username,
        password=password
      )
      
      if new_user is not None:
        Users.username=username
        Users.password=password
        Users.username.save_form_data(username)
        Users.password.save_form_data(password)
        new_user.save()
        login(request,new_user)
        return redirect('home/index.html')
      
  form=RegisterForm()
  

  
  return render(request, "registration/register.html",{
    "form": form
  })

def login(request):
  return render(request, "registration/login.html")

def about(request):
    return render(request, "home/about.html")



def products(request):
    return render(request, "home/products.html")
