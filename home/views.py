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
  if request.user.is_authenticated:
    user=request.user
    cartitems=Cart.objects.filter(user=user)

  amount=0.0
  shipping_amount=3.0
  total_amount=0.0
  cart_product=[p for p in Cart.objects.all() if p.user == user]
  if cart_product:
    for p in cart_product:
      tempamount=(p.quantity * p.items.price)
      amount += tempamount
      total_amount =amount+shipping_amount
    return render(request,'home/cart.html',{'carts':cartitems, 'totalamount':total_amount,'amount':amount})
  else:
    return render(request, 'home/emptycart.html')

def addtocart(request):
  user=request.user
  product_id=request.GET.get('prod_id')
  product=Product.objects.get(id=product_id)
  Cart(user=user,items=product).save()
  return redirect('/cart')

def checkout(request):
  user=request.user
  checkout = Cart.objects.filter(user=user)
  total_price=0.0
  item_price=[price for price in checkout]
  for val in item_price:
    total_price+=val.items.price
  
  
  return render(request, 'home/checkout.html',{'incheckout':checkout,'total_price':total_price})

def orders(request):
  user=request.user
  checkout = Cart.objects.filter(user=user)
  total_price=0.0
  item_price=[price for price in checkout]
  for val in item_price:
    total_price+=val.items.price

  person = [user for user in checkout]
  order_id=person[0].id
#  orders=Order(checkout)
#  order_id = (orders)
  
  #order_id=2
  
  return render(request,'home/orders.html',{'orderid':order_id,'incheckout':checkout,'total_price':total_price})