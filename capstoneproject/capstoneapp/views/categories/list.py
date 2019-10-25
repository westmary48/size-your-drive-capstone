import sqlite3
from django.shortcuts import render
from capstoneapp.models import Category
from capstoneapp.models import Item
from capstoneapp.models import model_factory
from ..connection import Connection


def category_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:

            conn.row_factory = model_factory(Category)

            db_cursor = conn.cursor()
            db_cursor.execute("""
            select
                c.id,
                c.name
            from capstoneapp_category c
            """)

            all_items = db_cursor.fetchall()

        template = 'items/list.html'
        context = {
            'all_items': all_items
        }

        return render(request, template, context)