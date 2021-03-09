from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Rank(models.Model):
    name = models.CharField(max_length=200,null=False)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)

    def _str_(self):
        return str(self.user)

    def can_make_loan(self):
        rank = Rank.objects.get(pk=self.rank)
        if rank == 'basic':
            return False
        else:
            return True


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)

class AccountType(models.Model):
    name = models.CharField(max_length=200, null=False)

class Ledger(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2)
    text = models.CharField(max_length=200,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction_id = models.PositiveIntegerField

