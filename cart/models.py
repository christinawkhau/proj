from django.db import models
from datetime import datetime
from accounts.models import Account
from products.models import Product

class Cart(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    #product_image = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.account.account} - {self.product.product_name} ({self.quantity}) - {self.total_price}"
