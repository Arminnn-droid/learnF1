from django.db import models

# Create your models here.

class Bank(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self) -> str:
        return self.name

class BankAccount(models.Model):
    bank =            models.ForeignKey(Bank, on_delete=models.CASCADE)
    balance =         models.DecimalField(max_digits=18, decimal_places=2)
    account_number =  models.IntegerField()
    types = (
        ('c', 'checking account'),
        ('s', 'savings account'),
    )
    type_selection =  models.CharField('account type', max_length=1, choices=types )
    
    def __str__(self) -> str:
        return self.account_number

class CheckingAccount(models.Model):
    balance =           models.DecimalField(max_digits=18, decimal_places=2)
    date_created =      models.DateField()
    last_transaction =  models.DateField()
    account_number =    models.ManyToManyField(BankAccount.account_number)
    
    def __str__(self) -> str:
        return self.account_number
    
    def deposit(cash, self):
        self.balance += cash
    
    def check_balance(self):
        return self.balance
    
    def withdrawal(self, cash):
        self.balance -= cash

class SavingsAccount(models.Model):
    balance =         models.DecimalField(max_digits=18, decimal_places=2)
    date_created =    models.DateField()
    account_number =  models.ManyToManyField(BankAccount.account_number)
    
    def __str__(self) -> str:
        return self.account_number
    
    def deposit(cash, self):
        self.balance += cash
    
    def check_balance(self):
        return self.balance
