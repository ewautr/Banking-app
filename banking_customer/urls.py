from django.contrib import admin
from django.urls import path

from . import views

app_name = 'banking_customer'

urlpatterns = [
   path('', views.index, name='index'),
   path('activity/<account_id>', views.activity, name='activity'),
   path('transfers/<account_id>', views.transfers, name='transfers'),
]
