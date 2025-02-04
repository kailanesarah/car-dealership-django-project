from django.contrib import admin
from .models import Brand, Car, CarInventory

# Registro do Model Brand
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']
    list_filter = ['name']

# Registro do Model Car
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id','model', 'factory_year', 'model_year', 'value', 'photo']
    search_fields = ['model', 'brand__name']  
    list_filter = ['brand', 'factory_year', 'model_year']
    ordering = ['id', 'factory_year']
    

# Registro do Model CarInventory
@admin.register(CarInventory)
class CarInventoryAdmin(admin.ModelAdmin):
    list_display = ['id','cars_count', 'cars_value', 'created_at']
    search_fields = ['car__model', 'car__brand__name']  
    list_filter = ['created_at']
    ordering = ['-created_at']
    list_per_page = 10 
    
