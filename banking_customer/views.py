from django.shortcuts import render, get_object_or_404
from banking_employee.models import Customer, Account

# Create your views here.

def index(request):
    customer = get_object_or_404(Customer, user=request.user)
    accounts = Account.objects.filter(customer=customer.pk)
    context = {
        'customer': customer,
        'accounts': accounts
     }
    return render(request, 'banking_customer/index.html', context)

def activity(request, account_id):
    activities = Account.objects.filter(pk=account_id)
    context = {
        'activities': activities
    }
    return render(request, 'banking_customer/activity.html', context)

def transfers(request, account_id):
    context ={}
    return render(request, 'banking_customer/transfers.html', context)