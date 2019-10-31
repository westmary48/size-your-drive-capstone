from django.db import models
from .item import Item


class ItemDonationBox(models.Model):
    """
    Creates the join table for the many to many relationship between items and donationboxes
    """

    item = models.OneToOneField(Item, on_delete=models.DO_NOTHING, null=True)
    is_donated = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_donated = models.DateTimeField(null=True)



    def __str__(self):
        return self.item.name