from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.


class MyUser(AbstractUser):
    img_profile = models.ImageField(upload_to='user', null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    USER_TYPE_DJANGO = 'D'
    USER_TYPE_FACEBOOK = 'F'
    USER_TYPE_GOOGLE = 'G'
    USER_TYPE_NAVER = 'N'

    USER_TYPE_CHOICES = (
        (USER_TYPE_DJANGO, 'Django'),
        (USER_TYPE_FACEBOOK, 'Facebook'),
        (USER_TYPE_GOOGLE, 'Google'),
        (USER_TYPE_NAVER, 'Naver'),
    )

    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default=USER_TYPE_DJANGO)
    nickname = models.CharField(max_length=24, null=True, unique=True)
    email = models.EmailField(null=True, blank=True)
