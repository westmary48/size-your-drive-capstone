import sqlite3
from django.shortcuts import render
from capstoneapp.models import Donator
from ..connection import Connection


def list_donators(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            d.id,
            d.address,
            d.phone_number
            d.user_id,
            u.first_name,
            u.last_name,
            u.email
        from capstoneapp_donator d
        join auth_user u on l.user_id = u.id
        """)

        all_donators = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            d = Donator()
            d.id = row["id"]
            d.address = row["address"]
            d.phone_number = row["phone_number"]
            d.user_id = row["user_id"]
            d.first_name = row["first_name"]
            d.last_name = row["last_name"]
            d.email = row["email"]

            all_donators.append(d)

    template_name = 'donators/list.html'

    context = {
        'all_donators': all_donators
    }

    return render(request, template_name, context)