from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Users, Customer,Category,Product,Order,OrderDetails,Cart
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib import messages

# Create your views here.
def home(request):
  return render(request, "home/index.html")

class ProductView(View):
  def get(self, request,data=None):
    if data==None:
      products=Product.objects.all()
    elif data == 1 or data == 2 or data ==3:
      products=Product.objects.filter(foodcategory=data)
      
    return render(request,'home/products.html',{
      'products':products
    })



class ProductSpecificView(View):
  def get(self, request, pk):
    product=Product.objects.get(pk=pk)
    return render(request,'home/productspecific.html',{
      'product':product
    })

    



class RegisterView(View):
  def get(self,request):
    form=RegisterForm()
    return render(request,'registration/register.html',{
      'form':form
    })
    
  def post(self,request):
      
    form=RegisterForm(request.POST)
    if form.is_valid():
      messages.success(request,'Congratulations! Registered successfully')
      form.save()
    return render(request,'registration/register.html',{
      'form':form
    })
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  """
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
"""
  
def login(request):
  return render(request, "registration/login.html")

def about(request):
    return render(request, "home/about.html")



#def products(request):
#    return render(request, #"home/products.html")

def productspecific(request):
  return render(request, "home/productspecific.html")

def cart(request):
  return render(request,'home/cart.html')