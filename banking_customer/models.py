from django.db import models
import uuid
from django.contrib.auth.models import User
from banking_employee.models import Account

# Create your models here.

class Ledger(models.Model):
    fromAccount = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="fromAccount")
    toAccount = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="toAccount")
    amount = models.IntegerField()
    text = models.CharField(null=True, max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)

    def __str__(self):
        return f"{self.fromAccount} - {self.toAccount} - {self.account} - {self.text} - {self.timestamp} - {self.transaction_id}"
