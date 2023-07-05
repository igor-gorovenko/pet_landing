from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime


class Advantage(models.Model):
    ''' Advatage in product '''

    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self) -> str:
        return f'{self.title}'
    

class Product(models.Model):
    ''' Product '''

    title = models.CharField(max_length=40)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='images')
    advantages = models.ManyToManyField(Advantage)
    
    def __str__(self) -> str:
        return f'{self.title}'
    

class Order(models.Model):
    ''' Order client '''
    create_order = models.DateField(auto_now=True)
    customer = models.CharField(max_length=40)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'order: {self.customer} {self.product} {self.create_order}'
