from django.db import models
from datetime import datetime
from accounts.models import Account
from products.models import Product

class order(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    product_image = models.URLField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account.accountname} - {self.product.product_name} ({self.quantity})"


def __str__(self):
    return f"{self.account.account} - {self.product.product_name} ({self.quantity}) - ${self.product.price}"
