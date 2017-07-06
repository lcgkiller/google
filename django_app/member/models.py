from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.

class User(AbstractUser):

    birth_date = models.DateField(null=True, blank=True)
