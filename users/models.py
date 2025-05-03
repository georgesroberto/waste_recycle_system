from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    """
    Custom user model with email as the unique identifier
    """
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    is_verified = models.BooleanField(default=False)
    
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.username
    
