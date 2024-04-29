from django.db import models
from users.models import User

class Products(models.Model):
    name=models.CharField(max_length=255)
    price=models.CharField(max_length=50)
    order=models.ForeignKey('users.User',on_delete=models.CASCADE,related_name='order')
    
    def __str__(self):
        return self.name
    
