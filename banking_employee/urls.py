from django.contrib import admin
from django.urls import path

from . import views

app_name = 'banking_employee'

urlpatterns = [
   path('', views.index, name='index'),
   path('addcustomer', views.addcustomer, name='addcustomer'),
   path('addaccount', views.addaccount, name='addaccount'),
   path('editcustomer/<customer_id>', views.editcustomer, name='editcustomer'),
]
