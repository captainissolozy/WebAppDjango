# Create your models here.
from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
