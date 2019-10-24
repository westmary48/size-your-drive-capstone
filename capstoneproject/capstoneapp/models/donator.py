from django.db import models
from django.contrib.auth.models import User


class Donator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    class Meta:
        verbose_name = ("donator")
        verbose_name_plural = ("donators")

