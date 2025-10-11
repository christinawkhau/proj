from django.db import models
from datetime import datetime
from accounts.models import Account
from products.models import Product


class notification(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    message_title = models.TextField (max_length=100)
    message=models.TextField()
    type=models.TextField()
    sent_at=models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField()
    
    def __str__(self):
        return f"{self.message}"
