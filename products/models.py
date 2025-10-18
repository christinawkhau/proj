from django.db import models
from datetime import datetime
from django.urls import reverse
from . choices import name_choices, brand_choices, price_choices
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=20, choices=name_choices.items())
    description = models.TextField(max_length=1000)
    category_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    
    
    
    # def get_absolute_url(self):
    #     return reverse('products', args=[str(self.id)])
    def __str__(self):
        return self.name
    
TAG = [
    ("New", "New"),
    ("Sale", "Sale"),
    ("Featured", "Featured"),
    ("Limited", "Limited"),
]

# Create your models here.
class Product(models.Model):
    sku = models.TextField(max_length=20)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2, choices=price_choices.items())
    stock = models.IntegerField(default=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    tag = models.CharField(choices=TAG, max_length=20)
    brand = models.CharField(max_length=20, choices=brand_choices.items())
    product_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    product_img1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    product_img2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    
    def __str__(self):      
        return f"{self.name} - {self.category}"
     
   
  