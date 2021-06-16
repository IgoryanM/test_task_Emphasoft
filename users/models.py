from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='age', default=18)
    email = models.EmailField(verbose_name='email', unique=True, blank=True)
