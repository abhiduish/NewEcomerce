from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.
users = (
    ('admin', 'admin'),
    ('shopuser', 'shopuser'),
    ('customer','customer')
)
class Customuser(AbstractUser):
 
    usertype = models.CharField(max_length=20,choices=users,default='admin')
    gender = models.CharField(max_length=30,blank=True)
    objects  = UserManager()
