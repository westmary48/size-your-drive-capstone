import sqlite3
from django.shortcuts import render
from django.urls import reverse
from rest_framework.viewsets import ViewSet
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import action
from capstoneapp.models import Item, DonationBox, Donator
from django.contrib.auth.models import User
from capstoneapp.models import model_factory
from ..connection import Connection


def donation_list(request):

    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:

            user = request.user

            conn.row_factory = model_factory(DonationBox)

            db_cursor = conn.cursor()
            db_cursor.execute("""
            select
                db.id,
                db.donator_id,
                db.created_date,
                db.item_id
            from capstoneapp_donationbox db
            where db.donator_id = ?

            """,(user.id,))

        all_donations = db_cursor.fetchall()

        template = 'donationbox/list.html'
        context = {
            'all_donations': all_donations
        }

        return render(request, template, context)



    elif request.POST.get('type') and request.POST.get('type') == "donation":
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO capstoneapp_donationbox
                (
                   donator_id
                )
                VALUES (?)
                """),

            (form_data['donator_id'])


            return redirect(reverse('capstoneapp:donations'))




            # newdonation = DonationBox()
            # newdonation.created_date = request.data["created_date"]
            # donator = Donator.objects.get(id=request.data["donator_id"])
            # newdonation.donator = donator
            # newdonation.save()


        # def add_to_box(request, item_id):
        #     item = Item.objects.get(id=item_id)
        #     donationbox = DonationBox(request)
        #     donationbox.add(item, item.name)

        # def remove_from_box(request, item_id):
        #     item = Item.objects.get(id=item_id)
        #     donationbox = DonationBox(request)
        #     donationbox.remove(item)

        # def get_donation(request):
        #     return render(request, 'donation.html', {'donation': DonationBox(request)})



    user = request.user
    donator = Donator.objects.get(pk=user.id)

    if request.method == 'GET':
        try:
            user_donations = donator.items.all()
        except Donator.DoesNotExist:
            user_donations = []


        template_name = "donationbox/list.html"
        return render(request, template_name, {'all_donations': user_donations})