from django.db import models

# Create your models here.

class Clients(models.Model):
    name =     models.CharField(max_length=300)
    company =  models.CharField(max_length=300)
    
    def __str__(self) -> str:
        return self.company

class Manufacturers(models.Model):
    name =      models.CharField(max_length=300)
    location =  models.TextField("address")
    
    def __str__(self) -> str:
        return self.name

class Products(models.Model):
    cost_per_item =    models.PositiveBigIntegerField("Cost")
    name_of_product =  models.CharField("name", max_length=300)
    manufacturer =     models.ForeignKey(Manufacturers, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
            return self.name
    
class ClientOrders(models.Model):
    fulfill_date =  models.PositiveIntegerField("Fulfill Month")
    order_number =  models.PositiveIntegerField(primary_key=True)
    client =        models.ForeignKey(Clients, on_delete=models.CASCADE)
    products =      models.ManyToManyField(Products)
    
    def __str__(self) -> str:
        return self.client
