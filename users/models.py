from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number=models.CharField(max_length=14,null=True,blank=True)
    image=models.ImageField(upload_to='image',default='image/default.jpeg')
    
    
    def __str__(self):
        return self.first_name
