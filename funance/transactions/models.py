from django.db import models

# Create your models here.
class Transaction(models.Model):
    class TransactionType(models.IntegerChoices):
        INCOME = 1
        EXPENSE = 2
        TRANSFER = 3
    transaction_type = models.IntegerField(choices=TransactionType)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10,decimal_places=2)