from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  path("", views.home, name="home"),  
  path("home/", views.home, name="home"),  
  path("register/",views.register,name="register"),
  path("login/",views.login,name="login"),
  path("about/",views.about,name="about"),
  path("products/",views.products,name="products")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)