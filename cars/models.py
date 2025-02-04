
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True)  

    def __str__(self):
        return self.name

class Car(models.Model):
    model = models.CharField(max_length=200)  
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='cars')  
    factory_year = models.PositiveIntegerField() 
    model_year = models.PositiveIntegerField()
    value = models.FloatField()  
    photo = models.ImageField(upload_to='listCars/')  
    bio = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f'{self.brand} {self.model} ({self.model_year})'

class CarInventory(models.Model):  
    cars_count = models.PositiveIntegerField()  
    cars_value = models.FloatField()  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Inventário de {self.car.model}: {self.cars_count} carros - R$ {self.cars_value}'

    class Meta:
        ordering = ['-created_at']  
