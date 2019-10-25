from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .donator import Donator
from .category import Category


class Item(models.Model):
    name = models.CharField(max_length=50,)
    donator = models.ForeignKey(Donator, on_delete=models.DO_NOTHING, null=True, blank=True,)
    description = models.CharField(max_length=255,)
    quantity = models.IntegerField(validators=[MinValueValidator(0)],)
    created_date = models.DateField(default="0000-00-00", null=True, blank=True,)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    size = models.CharField(max_length=50,)

    class Meta:
        verbose_name = ("item")
        verbose_name_plural = ("items")
