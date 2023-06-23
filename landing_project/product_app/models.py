from django.db import models


class Advantage(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self) -> str:
        return f'{self.title}'
    

class Product(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    price = models.IntegerField()
    advantages = models.ManyToManyField(Advantage)
    
    def __str__(self) -> str:
        return f'{self.title}'