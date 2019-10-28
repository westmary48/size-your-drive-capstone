from django.shortcuts import render
from django.views.generic import View
from django.utils import timezone
from .models import *
from .render import Render


class Pdf(View):

    def get(self, request):
        Item = Item.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'items': items,
            'request': request
        }
        return Render.render('pdf.html', params)
