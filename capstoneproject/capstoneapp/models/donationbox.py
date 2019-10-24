from django.db import models
from .donator import Donator


class DonationBox(models.Model):
    donator = models.ForeignKey(Donator, on_delete=models.DO_NOTHING)
    created_date = models.DateField(default="0000-00-00",)

    class Meta:
        verbose_name = ("donationbox")
        verbose_name_plural = ("donationboxes")
