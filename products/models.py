from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    isActive = models.BooleanField(default=True)
    
    def __str__(self):      
        return self.title
        