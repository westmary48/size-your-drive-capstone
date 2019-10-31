from django.db import models
from .donator import Donator
from .item import Item


class DonationBox(models.Model):
    item = models.ForeignKey(Item,  on_delete=models.DO_NOTHING)
    donator = models.ForeignKey(Donator, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now=True, null=True, blank=True,)
    complete = models.BooleanField(default=False, null=True, blank=True,)

    class Meta:
        verbose_name = ("donationbox")
        verbose_name_plural = ("donationboxes")


