from django.db import models
from datetime import datetime

class Category(models.Model):
    name = models.TextField(max_length=20)
    description = models.TextField(max_length=1000)
    category_img = models.ImageField(upload_to='photos/%Y/%x/%d/')
        
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
    name = models.CharField(max_length=100, default=1)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    is_active=models.BooleanField(default=True)
    tag = models.CharField(default="New", choices=TAG, max_length=20)
    brand = models.CharField(max_length=20, default="")

    product_img = models.ImageField(upload_to="images", default="product.jpg")
    product_img1 = models.ImageField(upload_to="images", default="product.jpg")
    product_img2 = models.ImageField(upload_to="images", default="product.jpg")

        
    def __str__(self):      
        return f"{self.name} - {self.price}"
     
