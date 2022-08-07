from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('publish date')
    
    def __str__(self) -> str:
        return self.text

class choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    votes = models.ImageField(default=0)
    
    def __str__(self) -> str:
        return self.text
