from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    phone=models.IntegerField(null=True)

    def _str_(self):
        return f"{self.text} - {self.status}"
