from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30 ,help_text="it's person name", primary_key=True)
    star = models.IntegerField("nomre", unique=True)

    def __str__(self):
        return self.first_name
