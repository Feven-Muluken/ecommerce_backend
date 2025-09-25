from django.contrib.auth.models import AbstractUser #for custom user model 
from django.db import models

# Create your models here.
class User(AbstractUser):
  
  ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('user', 'User'),
  )
  role = models.CharField(max_length=10, choices= ROLE_CHOICES, default='user')
  username = models.CharField(max_length = 255, unique=True)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length = 255)
  
  USERNAME_FIELD = 'email' #using email as the login field
  REQUIRED_FIELDS = ['username'] #- tells Django what fields are required when creating a user via createsuperuser or programmatically.

  def __str__(self):
    return f"{self.email} ({self.role})"