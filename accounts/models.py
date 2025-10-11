
from django.db import models
from datetime import datetime

# Create your models here.

class Account(models.Model):
    account = models.TextField()
    email = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.account.account

    

    
    
    