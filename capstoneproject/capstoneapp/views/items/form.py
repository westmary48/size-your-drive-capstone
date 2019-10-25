import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from capstoneapp.models import Item
from capstoneapp.models import Category
from capstoneapp.models import model_factory
from ..connection import Connection


def get_categories():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Category)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            c.id,
            c.name
        from capstoneapp_category c
        """)

        return db_cursor.fetchall()

@login_required
def item_form(request):
    if request.method == 'GET':
        categories = get_categories()
        template = 'items/form.html'
        context = {
            'all_categories': categories
        }

        return render(request, template, context)