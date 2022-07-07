from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm
urlpatterns=[
  path("", views.home, name="home"),  
  path("home/", views.home, name="home"),  
  path("register/",views.RegisterView.as_view(),name="register"),
  path("accounts/login/",auth_views.LoginView.as_view(template_name='registration/login.html',authentication_form=LoginForm),name="login"),
  path("about/",views.about,name="about"),
  path('productspecific/<int:pk>',views.ProductSpecificView.as_view(),name="productspecific"),
  path("products/",views.ProductView.as_view(),name="products"),
  path("products/<int:data>",views.ProductView.as_view(),name="productsfilter"),
path("cart/",views.cart,name="cart"),





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)