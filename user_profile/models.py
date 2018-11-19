from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField('username', max_length=20, unique=True, db_index=True)
    name = models.CharField('name', max_length=20)
    surname = models.CharField('surname', max_length=20)
    phone_number = models.CharField('phone_number', max_length=11)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
