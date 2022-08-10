from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length= 300)
    age = models.PositiveIntegerField(default=0)
    address = models.GenericIPAddressField(null=True, blank=True)
    salary = models.DecimalField(decimal_places= 2, max_digits=18) 
