from django.shortcuts import render, redirect
from .forms import RegisterForm, UserInfoForm
from .models import User, Category, Product, Order, Cart, UserInfo
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def home(request):
    return render(request, "home/index.html")


class ProductView(View):
    def get(self, request, data=None):
        if data == None:
            products = Product.objects.all()
        elif data == 1 or data == 2 or data == 3:
            products = Product.objects.filter(foodcategory=data)

        return render(request, 'home/products.html', {'products': products})


class ProductSpecificView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'home/productspecific.html',
                      {'product': product})


class RegisterView(View):
    def get_success_url(self, user):
        return redirect('/home/')

    def get(self, request):
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):

        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,
                             'Congratulations! Registered successfully')
            form.save()
            self.get_success_url(user=request.user)

    #return HttpResponseRedirect(self.get_success_url())
        return render(request, 'registration/register.html', {'form': form})
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


#def login(request):
#   return render(request, "registration/login.html")


def about(request):
    return render(request, "home/about.html")


#def products(request):
#    return render(request, #"home/products.html")

#def productspecific(request):
#   return render(request, "home/productspecific.html")


def cart(request):
    if request.user.is_authenticated:
        user = request.user
        cartitems = Cart.objects.filter(user=user)

    amount = 0.0
    shipping_amount = 3.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.items.price)
            amount += tempamount
            total_amount = amount + shipping_amount
        return render(request, 'home/cart.html', {
            'carts': cartitems,
            'totalamount': total_amount,
            'amount': amount
        })
    else:
        return render(request, 'home/emptycart.html')


def pluscart(request):
    if request.method == 'GET':
        user = request.user
        prodid = request.GET['prodid']
        c = Cart.objects.get(Q(items=prodid) & Q(user=user))
        c.quantity += 1
        c.save()

        amount = 0.0
        shipping_amount = 3.0
        total_amount = 0.0
        cart_product = [
            p for p in Cart.objects.all() if p.user == request.user
        ]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.items.price)
                amount += tempamount

            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': amount + shipping_amount
            }
            return JsonResponse(data)


def minuscart(request):
    if request.method == 'GET':
        user = request.user
        prodid = request.GET['prodid']
        c = Cart.objects.get(Q(items=prodid) & Q(user=user))
        c.quantity -= 1
        c.save()

        amount = 0.0
        shipping_amount = 3.0
        total_amount = 0.0
        cart_product = [
            p for p in Cart.objects.all() if p.user == request.user
        ]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.items.price)
                amount += tempamount

            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': amount + shipping_amount
            }
            return JsonResponse(data)


def removecart(request):
    if request.method == 'GET':
        user = request.user
        prodid = request.GET['prodid']
        c = Cart.objects.get(Q(items=prodid) & Q(user=user))
        c.delete()

        amount = 0.0
        shipping_amount = 3.0
        total_amount = 0.0
        cart_product = [
            p for p in Cart.objects.all() if p.user == request.user
        ]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.items.price)
                amount += tempamount

            data = {'amount': amount, 'totalamount': amount + shipping_amount}
            return JsonResponse(data)


def addtocart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, items=product).save()
    return redirect('/cart')


def checkout(request):
    user = request.user
    checkout = Cart.objects.filter(user=user)
    total_price = 0.0
    item_price = [price for price in checkout]
    for val in item_price:
        total_price += val.items.price * val.quantity

    form = UserInfoForm(request.POST or None)
    if form.is_valid():
        messages.success(request, "info saved")
        form.save()
        print("ds")
    return render(request, 'home/checkout.html', {
        'form': form,
        'incheckout': checkout,
        'total_price': total_price + 3
    })


#  return render(request, 'home/checkout.html', {
#       'incheckout': checkout,
#      'total_price': total_price
# })


class OrdersView(View):
    def get(self, request):
        user = request.user
        checkout = Cart.objects.filter(user=user)
        total_price = 0.0
        item_price = [price for price in checkout]
        for val in item_price:
            total_price += val.items.price * val.quantity

    #    person = [user for user in checkout]
        order_id = person[0].id
        #  orders=Order(checkout)
        #  order_id = (orders)

        #order_id=2
      #    order=[]
       # for i in range(0,len(checkout)):
        #  checkout[i].items.foodname
  
    
      
        return render(
            request, 'home/orders.html', {
                'orderid': order_id,
                'incheckout': checkout,
                'total_price': total_price + 3
            })
        #            return render(request, 'home/orders.html',{'form':form})
        # else:
        #  form = UserInfoForm()
        # return render(request,'home/checkout.html',{'form':form})


"""
  def post(self, request):

        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,
                             'Congratulations! Registered successfully')
            form.save()
        return render(request, 'registration/register.html', {'form': form})
"""


def profile(request):
    user = request.user
    #  print(user)
    #  userinfo = UserInfo.objects.get()
    print(userinfo)
    # print(userinfo)
    userinfo = 1
    return render(request, 'home/profile.html', {'userinfo': userinfo})
