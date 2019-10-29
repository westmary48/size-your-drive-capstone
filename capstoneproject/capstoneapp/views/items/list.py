import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from capstoneapp.models import Item
from capstoneapp.models import model_factory
from ..connection import Connection


@login_required
def item_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:

            conn.row_factory = model_factory(Item)

            db_cursor = conn.cursor()
            db_cursor.execute("""
            select
                i.id,
                i.name,
                i.description,
                i.size,
                i.quantity,
                i.category_id,
                i.donator_id
            from capstoneapp_item i
            """)

            all_items = db_cursor.fetchall()

        template = 'items/list.html'
        context = {
            'all_items': all_items
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO capstoneapp_item
            (
                name, description, size,
                quantity, donator_id, category_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (form_data['name'], form_data['description'],
                form_data['size'], form_data['quantity'],
                request.user.donator.id,
                 form_data["category_id"]))


    return redirect(reverse('capstoneapp:items'))

