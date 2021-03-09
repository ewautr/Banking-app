from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(null=True, max_length=200)
    
    class Rank(models.TextChoices):
        BASIC = 'Basic'
        SILVER = 'Silver'
        GOLD = 'Gold'

    rank = models.CharField(choices=Rank.choices, default=Rank.BASIC, max_length=200)

    def __str__(self):
        return f"{self.user} - {self.phone} - {self.rank}"

    @property
    def can_make_loan(self):
        if self.rank == 'Basic':
            return False
        else:
            return True



class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class AccountType(models.TextChoices):
        BANK_ACCOUNT = 'Bank Account'
        LOAN = 'Loan'

    account_type = models.CharField(choices=AccountType.choices, default=AccountType.BANK_ACCOUNT, max_length=200)
    balance = models.IntegerField(default=100)

    def __str__(self): 
        return f"{self.customer} - {self.account_type} - {self.balance}"

        