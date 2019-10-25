import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from capstoneapp.models import Item, Category
from capstoneapp.models import model_factory
from ..connection import Connection


def get_item(item_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Item)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            i.id,
            i.name,
            i.description,
            i.size,
            i.quantity,
            i.created_date,
            i.donator_id,
            i.category_id
        FROM capstoneapp_item i
        WHERE i.id = ?
        """, (item_id,))

        return db_cursor.fetchone()

@login_required

@login_required
def item_details(request, item_id):
    if request.method == 'GET':
        item = get_item(item_id)
        template_name = 'items/detail.html'
        return render(request, template_name, {'item': item})

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE capstoneapp_item
                SET name = ?,
                    description = ?,
                    size = ?,
                    quantity = ?,
                    category_id = ?
                WHERE id = ?
                """,
                (
                    form_data['name'], form_data['description'],
                    form_data['size'], form_data['quantity'],
                    form_data["category_id"], item_id,
                ))

            return redirect(reverse('capstoneapp:items'))

        # Check if this POST is for deleting a book
        #
        # Note: You can use parenthesis to break up complex
        #       `if` statements for higher readability
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM capstoneapp_item
                WHERE id = ?
                """, (item_id,))

            return redirect(reverse('capstoneapp:items'))
