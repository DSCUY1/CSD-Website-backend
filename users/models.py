from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Permission(models.Model):
    name = models.CharField(max_length=255)


class Role(models.Model):
    name = models.CharField(max_length=255)
    permissions = models.ManyToManyField(Permission)


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    matricule = models.CharField(max_length=7, default="0000000")
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
