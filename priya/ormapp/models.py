from django.db import models
from django.contrib import admin
class Product (models.Model):
    product_id=models.CharField(primary_key=True,max_length=8)
    product_name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    brand=models.CharField(max_length=50)
    stock_quantity=models.CharField(max_length=10)

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_id','product_name','price','brand','stock_quantity')


