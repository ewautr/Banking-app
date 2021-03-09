from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from banking_employee.models import Customer, Account

# Create your views here.
def index(request):
    customers = Customer.objects.all()
    accounts = Account.objects.all()
    context = {'customers': customers, 'accounts': accounts}

    return render(request, 'banking_employee/index.html', context)

def addcustomer(request):
    context = {}

    if request.method == 'POST':
        user_name = request.POST['user_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        rank = request.POST['rank']

        if password != confirmPassword:
            context = {
                'error': 'Passwords did not match. Please try again.'
            }
            return render(request, 'banking_employee/addcustomer.html', context)

        new_user = User.objects.create_user(user_name, email, password)

        customer = Customer()
        customer.user = new_user
        customer.phone = phone
        customer.rank = rank
        customer.save()

    return render(request, 'banking_employee/addcustomer.html', context)

def editcustomer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    context = { 'customer': customer }

    if request.method == 'POST':
        user = customer.user
        user.user_name = request.POST['user_name']
        customer.phone = request.POST['phone']
        customer.rank = request.POST['rank']
        customer.save()
        user.save()
        return redirect('banking_employee:index')

    return render(request, 'banking_employee/editcustomer.html', context)

def addaccount(request):
    customers = Customer.objects.all()
    context = {'customers': customers}

    if request.method == 'POST':
        customerPK = request.POST['customer']
        account_type = request.POST['account_type']
        customer = get_object_or_404(Customer, pk=customerPK)

        account = Account()
        account.customer = customer
        account.account_type = account_type
        account.save()

        return redirect('banking_employee:index')

    return render(request, 'banking_employee/addaccount.html', context)