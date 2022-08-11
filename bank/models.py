from turtle import mode
from django.db import models

# Create your models here.

class Bank(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self) -> str:
        return self.name

class BankAccount(models.Model):
    bank = models.ForeignKey(on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=18, decimal_places=2)
    account_number = models.IntegerField(max_length=18)
    types = (
        ('c', 'checking account'),
        ('s', 'savings account'),
    )
    type_selection = models.CharField('account type', max_length=1, choices=types )
    
    def __str__(self) -> str:
        return self.balance

class CheckingAccount(models.Model):
    pass

class SavingsAccount(models.Model):
    pass
