from django.contrib import admin
from .models import ProductModel

@admin.register(ProductModel)
class Productadmin(admin.ModelAdmin):
    list_display = ['user','pname','img','price','quantity']

# Register your models here.
