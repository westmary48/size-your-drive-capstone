from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url
from capstoneapp.models import *
from capstoneapp import views
from .views import *
from django.conf.urls import url


app_name = "capstoneapp"

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    url(r'^items$', item_list, name='items'),
]