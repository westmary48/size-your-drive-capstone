from django.conf.urls import url
from .views import *

app_name = "capstoneapp"

urlpatterns = [
    url(r'^$', item_list, name='home'),
    url(r'^items$', item_list, name='items'),
]