from django.contrib import admin
from .models importz Users, Customer,Category,Product,Order,OrderDetails,Cart

# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
  list_display=['id','user','name','address']

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
  list_display=['id','foodtype','typedesc']
  
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
  list_display=['id','foodcategory','foodname','foodimg','fooddesc','price']
  
@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
  list_display=['id','user','date','status']
  
@admin.register(OrderDetails)
class OrderDetailsModelAdmin(admin.ModelAdmin):
  list_display=['orderid','foodid','quantity']
  
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
  list_display=['id','user','items','quantity']
